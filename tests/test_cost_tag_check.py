import json

from scripts.cost_tag_check import check_plan


def test_fixture_plan_flags_missing_landlord_account_tags(capsys):
    result = check_plan("fixtures/plan.json")

    captured = capsys.readouterr()

    assert result == 1
    assert "aws_s3_bucket.listing_media" in captured.out
    assert "aws_lambda_function.mls_feed_sync" in captured.out

    assert "aws_s3_bucket.landlord_media[0]" not in captured.out
    assert "aws_lambda_function.screening_report_export" not in captured.out


def test_cost_tag_check_is_idempotent(tmp_path, capsys):
    plan = {
        "resource_changes": [
            {
                "address": "aws_s3_bucket.example",
                "change": {
                    "actions": ["create"],
                    "after": {"tags": {}}
                }
            }
        ]
    }

    plan_file = tmp_path / "plan.json"
    plan_file.write_text(json.dumps(plan), encoding="utf-8")

    first_result = check_plan(str(plan_file))
    first_output = capsys.readouterr().out

    second_result = check_plan(str(plan_file))
    second_output = capsys.readouterr().out

    assert first_result == second_result == 1
    assert first_output == second_output
    assert first_output.count("aws_s3_bucket.example") == 1


def test_resources_without_create_or_update_are_skipped(tmp_path, capsys):
    plan = {
        "resource_changes": [
            {
                "address": "aws_s3_bucket.unchanged",
                "change": {
                    "actions": ["no-op"],
                    "after": {"tags": {}}
                }
            }
        ]
    }

    plan_file = tmp_path / "plan.json"
    plan_file.write_text(json.dumps(plan), encoding="utf-8")

    result = check_plan(str(plan_file))
    captured = capsys.readouterr()

    assert result == 0
    assert "aws_s3_bucket.unchanged" not in captured.out
