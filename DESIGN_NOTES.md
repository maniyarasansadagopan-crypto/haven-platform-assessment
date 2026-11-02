# Design Notes

## B2 — idempotency key

State exactly what key your `cost_tag_check.py` uses to decide a plan has already been
checked/reported on. Use the word "idempotency" in your explanation.

<!-- Your answer here -->
   Why landlord_account_id is used instead of tenant_id.



Why the checker is stateless.



Which Terraform resource actions are checked.



How missing or empty tags are handled.



Why deterministic output matters.



How idempotency is achieved by the actual implementation.
## Any other decision with a non-obvious alternative

<!-- Your answer here -->
