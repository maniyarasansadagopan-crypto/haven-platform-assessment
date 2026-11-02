"""
Write tests here proving:
  1. A PropertyManager scoped to la-001 (pm-001) is DENIED access to la-002's tenant's
     screening report (rep-002).
  2. The same PropertyManager (pm-001) IS allowed access to their own account's screening
     report (rep-001).

Use the `property_managers`, `properties`, `tenants`, and `screening_reports` fixtures from
conftest.py — don't re-invent the seed data here.
"""
from app.access_control import can_access_screening_report


from app.access_control import can_access_screening_report
from app.models import PropertyManager, ScreeningReport, Property, Tenant


def test_manager_can_access_report_in_same_landlord_account():
    actor = PropertyManager("pm-001", "Manager", "la-001")
    report = ScreeningReport("rep-001", "tenant-001", "1234", 700)

    tenant = Tenant("tenant-001", "Tenant", "prop-001")
    property_record = Property("prop-001", "la-001", "Chennai")

    assert can_access_screening_report(
        actor,
        report,
        properties=[property_record],
        tenants=[tenant],
    ) is True


def test_manager_cannot_access_another_landlord_account():
    actor = PropertyManager("pm-001", "Manager", "la-001")
    report = ScreeningReport("rep-002", "tenant-002", "5678", 650)

    tenant = Tenant("tenant-002", "Tenant", "prop-002")
    property_record = Property("prop-002", "la-002", "Bangalore")

    assert can_access_screening_report(
        actor,
        report,
        properties=[property_record],
        tenants=[tenant],
    ) is False


def test_missing_tenant_denies_access():
    actor = PropertyManager("pm-001", "Manager", "la-001")
    report = ScreeningReport("rep-001", "missing-tenant", "1234", 700)

    assert can_access_screening_report(
        actor,
        report,
        properties=[],
        tenants=[],
    ) is False


def test_missing_property_denies_access():
    actor = PropertyManager("pm-001", "Manager", "la-001")
    report = ScreeningReport("rep-001", "tenant-001", "1234", 700)

    tenant = Tenant("tenant-001", "Tenant", "missing-property")

    assert can_access_screening_report(
        actor,
        report,
        properties=[],
        tenants=[tenant],
    ) is False
