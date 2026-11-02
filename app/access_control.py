"""
B2, part 1 — implement can_access_screening_report().

Read README.md's domain model first. A ScreeningReport belongs to a Tenant, a Tenant belongs to
a Property, and a Property belongs to a LandlordAccount. A PropertyManager is scoped to exactly
one LandlordAccount.

Work out from that hierarchy which boundary actually gates access to a ScreeningReport.
"""
from app.models import PropertyManager, ScreeningReport, Property, Tenant


def can_access_screening_report(
    actor: PropertyManager,
    report: ScreeningReport,
    *,
    properties: list[Property],
    tenants: list[Tenant],
) -> bool:
    """
    actor: the PropertyManager requesting access
    report: the ScreeningReport they're trying to view
    properties: all known Property records
    tenants: all known Tenant records

    Return True if actor may view report, False otherwise.
    Fail closed if any required relationship is missing.
    """

    # Check that the manager and report have required IDs
    if not actor.landlord_account_id or not report.tenant_id:
        return False

    # Find the tenant associated with the screening report
    tenant = next(
        (t for t in tenants if t.id == report.tenant_id),
        None
    )

    # Deny access if tenant is missing
    if tenant is None or not tenant.property_id:
        return False

    # Find the property associated with the tenant
    property_record = next(
        (p for p in properties if p.id == tenant.property_id),
        None
    )

    # Deny access if property is missing
    if property_record is None or not property_record.landlord_account_id:
        return False

    # Allow access only if landlord account IDs match
    return (
        actor.landlord_account_id
        == property_record.landlord_account_id
    )
    """
    actor: the PropertyManager requesting access
    report: the ScreeningReport they're trying to view
    properties: all known Property records
    tenants: all known Tenant records

    Return True if actor may view report, False otherwise. Fail closed — if anything needed to
    make this determination is missing (tenant not found, property not found), return False.
    """
    raise NotImplementedError("Implement this.")
