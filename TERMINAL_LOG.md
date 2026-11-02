# Terminal Log

Setup, B0 plan, both B2 test runs and the cost tag check run twice.

```text
ubuntu@ip-172-31-2-146:~$ tmux set-option -g history-limit 100000
ubuntu@ip-172-31-2-146:~$ cd ~
git clone https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
cd haven-platform-assessment
Cloning into 'haven-platform-assessment'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 50 (delta 10), reused 50 (delta 10), pack-reused 0 (from 0)
Receiving objects: 100% (50/50), 14.94 KiB | 3.73 MiB/s, done.
Resolving deltas: 100% (10/10), done.
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pwd
/home/ubuntu/haven-platform-assessment
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ ls -la
total 60
drwxrwxr-x 9 ubuntu ubuntu 4096 Nov  2 17:01 .
drwxr-x--- 6 ubuntu ubuntu 4096 Nov  2 17:01 ..
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 .ai-conversations
drwxrwxr-x 7 ubuntu ubuntu 4096 Nov  2 17:01 .git
-rw-rw-r-- 1 ubuntu ubuntu   83 Nov  2 17:01 .gitignore
-rw-rw-r-- 1 ubuntu ubuntu  187 Nov  2 17:01 B0.md
-rw-rw-r-- 1 ubuntu ubuntu  215 Nov  2 17:01 B1.md
-rw-rw-r-- 1 ubuntu ubuntu  307 Nov  2 17:01 DESIGN_NOTES.md
-rw-rw-r-- 1 ubuntu ubuntu 1396 Nov  2 17:01 README.md
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 app
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 fixtures
-rw-rw-r-- 1 ubuntu ubuntu   12 Nov  2 17:01 requirements.txt
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 scripts
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 terraform
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:01 tests
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git log --oneline
c32764f (HEAD -> main, origin/main, origin/HEAD) chore: polish README and stub comments
b295614 Add .gitignore, drop compiled bytecode from tracking
607b334 Haven platform infrastructure assessment — starter
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat README.md
# Haven — Platform Infrastructure Assessment

Haven is a multi-tenant real estate platform.

## Domain model

```
LandlordAccount  (the billing unit)
  └── Property
        └── Tenant
              └── ScreeningReport  (SSN, credit score)

PropertyManager  (scoped to exactly one LandlordAccount)
```

A `LandlordAccount` is the billing unit — every property, every tenant, every report underneath
it rolls up to exactly one. A `PropertyManager` is scoped to exactly one `LandlordAccount` and
everything under it.

This codebase currently tags and checks access using whatever ID happened to be on hand when
each piece was written — that reflects how it was built, not a spec to replicate.

## What not to modify

`app/seed_data.py`, `app/models.py`, `fixtures/plan.json`, `terraform/terraform.tfstate` — the
assignment's checks assume this data is unchanged.

`terraform/terraform.tfstate` is checked in deliberately, not an accident — it's a seeded state
representing 4 already-provisioned landlord media buckets, standing in for a real AWS account so
B0 can be reproduced with `terraform plan` instead of just reasoned about. See `terraform/main.tf`
for how to use it.

## Where things are

| Path | Task |
|---|---|
| `terraform/main.tf` | B0 |
| `terraform/lifecycle.tf` | B1 |
| `app/access_control.py`, `scripts/cost_tag_check.py` | B2 — stubs to implement |
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ python3 --version
terraform version
git --version
Python 3.14.4
Terraform v1.9.8
on linux_amd64

Your version of Terraform is out of date! The latest version
is 1.17.1. You can update by downloading from https://www.terraform.io/downloads.html
git version 2.53.0
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ python3 -m venv .venv
ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ source .venv/bin/activate
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pip install -r requirements.txt
Collecting pytest>=8.0 (from -r requirements.txt (line 1))
  Downloading pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
Collecting iniconfig>=2 (from pytest>=8.0->-r requirements.txt (line 1))
  Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging>=24 (from pytest>=8.0->-r requirements.txt (line 1))
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.6 (from pytest>=8.0->-r requirements.txt (line 1))
  Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting pygments>=2.15 (from pytest>=8.0->-r requirements.txt (line 1))
  Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Downloading pytest-9.2.0-py3-none-any.whl (411 kB)
Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 71.6 MB/s eta 0:00:00
Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest
Successfully installed iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.2.0
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest --version
pytest 9.2.0
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd terraform
terraform init
cd ..
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 5.0"...
- Installing hashicorp/aws v5.100.0...
- Installed hashicorp/aws v5.100.0 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest -q

no tests ran in 0.01s
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd
(.venv) ubuntu@ip-172-31-2-146:~$ haven-platform-assessment/terraform/
-bash: haven-platform-assessment/terraform/: Is a directory
(.venv) ubuntu@ip-172-31-2-146:~$ haven-platform-assessment/terraform
-bash: haven-platform-assessment/terraform: Is a directory
(.venv) ubuntu@ip-172-31-2-146:~$ ls
haven-platform-assessment
(.venv) ubuntu@ip-172-31-2-146:~$ cd haven-platform-assessment/
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat terraform/variables.tf
variable "landlord_accounts" {
  type        = list(string)
  description = "Landlord account IDs, in the order their infra was originally provisioned."
  default     = ["la-001", "la-002", "la-003", "la-004"]
}
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ terraform plan -refresh=false -no-color | tail -15

Error: No configuration files

Plan requires configuration to be present. Planning without a configuration would mark everything for destruction, which is normally not what is desired.
If you would like to destroy everything, run plan with the -destroy option. Otherwise, create a Terraform configuration file (.tf file) and try again.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat terraform/main.tf
# B0 — The `count` trap
#
# Each landlord account gets a dedicated S3 bucket for their media, addressed by POSITION in
# var.landlord_accounts. This is the setup the assignment asks you to reason about: what happens
# to `terraform plan` when an account in the middle of the list is removed?
#
# Try it: this directory ships with a `terraform.tfstate` already seeded with all 4 buckets, so
# you don't need a real AWS account or `terraform apply` to see this. Remove "la-002" from
# variables.tf's default list, then run:
#
#   terraform plan -refresh=false
#
# The -refresh=false matters: a plain `terraform plan` tries to refresh each resource against
# real AWS first, the dummy credentials get a 403, and Terraform quietly drops the "missing"
# resource from state and plans a fresh create instead — which hides the bug entirely. Skipping
# the refresh diffs your config directly against the seeded state, which is what shows the real
# destroy/recreate cascade.

resource "aws_s3_bucket" "landlord_media" {
  count  = length(var.landlord_accounts)
  bucket = "haven-media-${var.landlord_accounts[count.index]}"

  tags = {
    landlord_account_id = var.landlord_accounts[count.index]
  }
}
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd terraform
terraform plan -refresh=false -no-color | tail -15
cd ..

  with aws_s3_bucket_lifecycle_configuration.listing_media_archive,
  on lifecycle.tf line 15, in resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive":
  15: resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {

No attribute specified when one (and only one) of [rule[0].filter,rule[0].prefix] is required

This will be an error in a future version of the provider

(and one more similar warning elsewhere)

─────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano terraform/lifecycle.tf
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git diff -- terraform/lifecycle.tf
diff --git a/terraform/lifecycle.tf b/terraform/lifecycle.tf
index d89f089..f13f00b 100644
--- a/terraform/lifecycle.tf
+++ b/terraform/lifecycle.tf
@@ -18,6 +18,8 @@ resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {
   rule {
     id     = "archive-sold-listing-photos"
     status = "Enabled"
+
+    filter {}

     transition {
       days          = 30
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd terraform
terraform plan -refresh=false -no-color
cd ..

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.listing_media will be created
  + resource "aws_s3_bucket" "listing_media" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "haven-listing-media"
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags_all                    = (known after apply)
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + cors_rule (known after apply)

      + grant (known after apply)

      + lifecycle_rule (known after apply)

      + logging (known after apply)

      + object_lock_configuration (known after apply)

      + replication_configuration (known after apply)

      + server_side_encryption_configuration (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

  # aws_s3_bucket_lifecycle_configuration.listing_media_archive will be created
  + resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {
      + bucket                                 = (known after apply)
      + expected_bucket_owner                  = (known after apply)
      + id                                     = (known after apply)
      + transition_default_minimum_object_size = "all_storage_classes_128K"

      + rule {
          + id     = "archive-sold-listing-photos"
          + status = "Enabled"
            # (1 unchanged attribute hidden)

          + filter {
                # (1 unchanged attribute hidden)
            }

          + transition {
              + days          = 30
              + storage_class = "GLACIER"
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano terraform/variables.tf
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git diff -- terraform/variables.tf
diff --git a/terraform/variables.tf b/terraform/variables.tf
index 8ae62bd..0f8a686 100644
--- a/terraform/variables.tf
+++ b/terraform/variables.tf
@@ -1,5 +1,5 @@
 variable "landlord_accounts" {
   type        = list(string)
   description = "Landlord account IDs, in the order their infra was originally provisioned."
-  default     = ["la-001", "la-002", "la-003", "la-004"]
+  default     = ["la-001", "la-003", "la-004"]
 }
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd terraform
terraform plan -refresh=false -no-color
cd ..

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # aws_s3_bucket.landlord_media[1] must be replaced
-/+ resource "aws_s3_bucket" "landlord_media" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      ~ bucket                      = "haven-media-la-002" -> "haven-media-la-003" # forces replacement
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      ~ id                          = "haven-media-la-002" -> (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      ~ tags                        = {
          ~ "landlord_account_id" = "la-002" -> "la-003"
        }
      ~ tags_all                    = {
          ~ "landlord_account_id" = "la-002" -> "la-003"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      ~ cors_rule (known after apply)

      ~ grant (known after apply)

      ~ lifecycle_rule (known after apply)

      ~ logging (known after apply)

      ~ object_lock_configuration (known after apply)

      ~ replication_configuration (known after apply)

      ~ server_side_encryption_configuration (known after apply)

      ~ versioning (known after apply)

      ~ website (known after apply)
    }

  # aws_s3_bucket.landlord_media[2] must be replaced
-/+ resource "aws_s3_bucket" "landlord_media" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      ~ bucket                      = "haven-media-la-003" -> "haven-media-la-004" # forces replacement
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      ~ id                          = "haven-media-la-003" -> (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      ~ tags                        = {
          ~ "landlord_account_id" = "la-003" -> "la-004"
        }
      ~ tags_all                    = {
          ~ "landlord_account_id" = "la-003" -> "la-004"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      ~ cors_rule (known after apply)

      ~ grant (known after apply)

      ~ lifecycle_rule (known after apply)

      ~ logging (known after apply)

      ~ object_lock_configuration (known after apply)

      ~ replication_configuration (known after apply)

      ~ server_side_encryption_configuration (known after apply)

      ~ versioning (known after apply)

      ~ website (known after apply)
    }

  # aws_s3_bucket.landlord_media[3] will be destroyed
  # (because index [3] is out of range for count)
  - resource "aws_s3_bucket" "landlord_media" {
      - bucket   = "haven-media-la-004" -> null
      - id       = "haven-media-la-004" -> null
      - tags     = {
          - "landlord_account_id" = "la-004"
        } -> null
      - tags_all = {
          - "landlord_account_id" = "la-004"
        } -> null
    }

  # aws_s3_bucket.listing_media will be created
  + resource "aws_s3_bucket" "listing_media" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "haven-listing-media"
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags_all                    = (known after apply)
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + cors_rule (known after apply)

      + grant (known after apply)

      + lifecycle_rule (known after apply)

      + logging (known after apply)

      + object_lock_configuration (known after apply)

      + replication_configuration (known after apply)

      + server_side_encryption_configuration (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

  # aws_s3_bucket_lifecycle_configuration.listing_media_archive will be created
  + resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {
      + bucket                                 = (known after apply)
      + expected_bucket_owner                  = (known after apply)
      + id                                     = (known after apply)
      + transition_default_minimum_object_size = "all_storage_classes_128K"

      + rule {
          + id     = "archive-sold-listing-photos"
          + status = "Enabled"
            # (1 unchanged attribute hidden)

          + filter {
                # (1 unchanged attribute hidden)
            }

          + transition {
              + days          = 30
              + storage_class = "GLACIER"
            }
        }
    }

Plan: 4 to add, 0 to change, 3 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git checkout -- terraform/variables.tf
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git status --short
 M terraform/lifecycle.tf
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano B0.md
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat B0.md
# B0 — The `count` trap

What does `terraform plan` show when a middle landlord account is removed from the list? Why is
that dangerous here? What's the fix?

<!-- Your answer here -->
The Terraform count-index shift problem.



The risk of destroying existing landlord media buckets.



Using for_each with landlord account IDs as keys.



Using Terraform moved blocks or terraform state mv to migrate existing state.



Optionally using prevent_destroy as an additional safeguard.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git add B0.md
git commit -m "B0: explain count-index shift and for_each/moved fix"
git push
[main b9bcb77] B0: explain count-index shift and for_each/moved fix
 1 file changed, 17 insertions(+)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 593 bytes | 593.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
   c32764f..b9bcb77  main -> main
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat terraform/lifecycle.tf
# B1 — The Glacier cost gotcha
#
# Sold listings' photos archive to Glacier 30 days after upload, to cut storage cost. Separately
# (not modeled in Terraform — it's an application-level flow), a seller can request deletion of
# their listing data, which must happen within 30 days of the request.
#
# Reason through: a photo archives to Glacier on day 30. The seller requests deletion on day 40.
# You delete it immediately. What does that actually cost, given Glacier's minimum storage
# duration, and what would you change here?

resource "aws_s3_bucket" "listing_media" {
  bucket = "haven-listing-media"
}

resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {
  bucket = aws_s3_bucket.listing_media.id

  rule {
    id     = "archive-sold-listing-photos"
    status = "Enabled"

    filter {}

    transition {
      days          = 30
      storage_class = "GLACIER"
    }
  }
}
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano B1.md
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat B1.md
# B1 — The Glacier cost gotcha

What's the actual cost impact of an early deletion after archival? How would you redesign the
lifecycle so this stops quietly costing more than budgeted?

<!-- Your answer here -->
The lifecycle rule transitions objects to Glacier after 30 days.



Glacier has a 90-day minimum storage duration, as described in the assignment.



If a seller requests deletion on day 40, the object has been in Glacier for only 10 days.



The remaining minimum-duration period is approximately 80 days.



Early deletion can result in remaining storage-duration charges and applicable request charges.



Discuss redesign options:
- Delay the Glacier transition until after the higher-risk deletion window.
- Consider a storage class without the same 90-day minimum.
- Manage deletion requests through grouping, tagging, or alerts.
- Check AWS S3 pricing before choosing the final approach.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git add B1.md
git commit -m "B1: Glacier 90-day minimum early-deletion cost and lifecycle redesign"
git push
[main 6d89097] B1: Glacier 90-day minimum early-deletion cost and lifecycle redesign
 1 file changed, 25 insertions(+)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 805 bytes | 805.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
   b9bcb77..6d89097  main -> main
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat app/models.py
cat app/seed_data.py
cat app/access_control.py
"""
Haven's tenancy model. Read README.md for how these fit together before you touch
access_control.py or cost_tag_check.py.

    LandlordAccount (billing unit)
      -> Property
           -> Tenant
                -> ScreeningReport

    PropertyManager is scoped to exactly one LandlordAccount.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class LandlordAccount:
    id: str
    name: str


@dataclass(frozen=True)
class Property:
    id: str
    landlord_account_id: str
    address: str


@dataclass(frozen=True)
class PropertyManager:
    id: str
    name: str
    landlord_account_id: str


@dataclass(frozen=True)
class Tenant:
    id: str
    name: str
    property_id: str


@dataclass(frozen=True)
class ScreeningReport:
    id: str
    tenant_id: str
    ssn_last4: str
    credit_score: int
"""
Seeded domain data for the assessment. Do not modify — the assignment's "must work" checks
assume this data is unchanged.

Two landlord accounts (la-001, la-002), each with one property, one property manager, one
tenant, and one screening report. Use this to reason about and test the cross-account denial
case in B2, part 1: a PropertyManager scoped to la-001 must never be able to access the
screening report belonging to la-002's tenant, and vice versa.
"""
from app.models import LandlordAccount, Property, PropertyManager, ScreeningReport, Tenant

LANDLORD_ACCOUNTS = [
    LandlordAccount(id="la-001", name="Maple Grove Holdings"),
    LandlordAccount(id="la-002", name="Birchwood Properties"),
]

PROPERTIES = [
    Property(id="prop-001", landlord_account_id="la-001", address="12 Maple St"),
    Property(id="prop-002", landlord_account_id="la-002", address="88 Birch Ave"),
]

PROPERTY_MANAGERS = [
    PropertyManager(id="pm-001", name="Asha Rao", landlord_account_id="la-001"),
    PropertyManager(id="pm-002", name="Leo Fontaine", landlord_account_id="la-002"),
]

TENANTS = [
    Tenant(id="ten-001", name="J. Alvarez", property_id="prop-001"),
    Tenant(id="ten-002", name="S. Okafor", property_id="prop-002"),
]

SCREENING_REPORTS = [
    ScreeningReport(id="rep-001", tenant_id="ten-001", ssn_last4="1234", credit_score=710),
    ScreeningReport(id="rep-002", tenant_id="ten-002", ssn_last4="5678", credit_score=690),
]
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

    Return True if actor may view report, False otherwise. Fail closed — if anything needed to
    make this determination is missing (tenant not found, property not found), return False.
    """
    raise NotImplementedError("Implement this.")
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano app/access_control.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano app/access_control.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_access_control.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 0 items

================================================================== no tests ran in 0.02s ===================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ ls -l tests/
total 16
-rw-rw-r-- 1 ubuntu ubuntu    0 Nov  2 17:01 __init__.py
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov  2 17:04 __pycache__
-rw-rw-r-- 1 ubuntu ubuntu  469 Nov  2 17:01 conftest.py
-rw-rw-r-- 1 ubuntu ubuntu  471 Nov  2 17:01 test_access_control.py
-rw-rw-r-- 1 ubuntu ubuntu  618 Nov  2 17:01 test_cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat tests/test_access_control.py
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
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat app/access_control.py
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
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat app/models.py
"""
Haven's tenancy model. Read README.md for how these fit together before you touch
access_control.py or cost_tag_check.py.

    LandlordAccount (billing unit)
      -> Property
           -> Tenant
                -> ScreeningReport

    PropertyManager is scoped to exactly one LandlordAccount.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class LandlordAccount:
    id: str
    name: str


@dataclass(frozen=True)
class Property:
    id: str
    landlord_account_id: str
    address: str


@dataclass(frozen=True)
class PropertyManager:
    id: str
    name: str
    landlord_account_id: str


@dataclass(frozen=True)
class Tenant:
    id: str
    name: str
    property_id: str


@dataclass(frozen=True)
class ScreeningReport:
    id: str
    tenant_id: str
    ssn_last4: str
    credit_score: int
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest --collect-only -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 0 items

=============================================================== no tests collected in 0.02s ================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ ls -la tests/
total 24
drwxrwxr-x  3 ubuntu ubuntu 4096 Nov  2 17:04 .
drwxrwxr-x 11 ubuntu ubuntu 4096 Nov  2 17:18 ..
-rw-rw-r--  1 ubuntu ubuntu    0 Nov  2 17:01 __init__.py
drwxrwxr-x  2 ubuntu ubuntu 4096 Nov  2 17:04 __pycache__
-rw-rw-r--  1 ubuntu ubuntu  469 Nov  2 17:01 conftest.py
-rw-rw-r--  1 ubuntu ubuntu  471 Nov  2 17:01 test_access_control.py
-rw-rw-r--  1 ubuntu ubuntu  618 Nov  2 17:01 test_cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano tests/test_access_control.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_access_control.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 4 items

tests/test_access_control.py::test_manager_can_access_report_in_same_landlord_account PASSED                                                         [ 25%]
tests/test_access_control.py::test_manager_cannot_access_another_landlord_account PASSED                                                             [ 50%]
tests/test_access_control.py::test_missing_tenant_denies_access PASSED                                                                               [ 75%]
tests/test_access_control.py::test_missing_property_denies_access PASSED                                                                             [100%]

==================================================================== 4 passed in 0.03s =====================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git add app/access_control.py
git commit -m "B2.1: gate screening report access on landlord account via tenant->property"
git push
[main ce11b20] B2.1: gate screening report access on landlord account via tenant->property
 1 file changed, 39 insertions(+)
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.11 KiB | 1.11 MiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
   6d89097..ce11b20  main -> main
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat tests/conftest.py
cat tests/test_access_control.py
import pytest

from app.seed_data import (
    LANDLORD_ACCOUNTS,
    PROPERTIES,
    PROPERTY_MANAGERS,
    SCREENING_REPORTS,
    TENANTS,
)


@pytest.fixture
def landlord_accounts():
    return LANDLORD_ACCOUNTS


@pytest.fixture
def properties():
    return PROPERTIES


@pytest.fixture
def property_managers():
    return PROPERTY_MANAGERS


@pytest.fixture
def tenants():
    return TENANTS


@pytest.fixture
def screening_reports():
    return SCREENING_REPORTS
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
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_access_control.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 4 items

tests/test_access_control.py::test_manager_can_access_report_in_same_landlord_account PASSED                                                         [ 25%]
tests/test_access_control.py::test_manager_cannot_access_another_landlord_account PASSED                                                             [ 50%]
tests/test_access_control.py::test_missing_tenant_denies_access PASSED                                                                               [ 75%]
tests/test_access_control.py::test_missing_property_denies_access PASSED                                                                             [100%]

==================================================================== 4 passed in 0.02s =====================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git add tests/test_access_control.py
git commit -m "B2.1: tests for cross-account denial, same-account allow, fail-closed"
git push
[main 24fb72f] B2.1: tests for cross-account denial, same-account allow, fail-closed
 1 file changed, 60 insertions(+)
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 938 bytes | 938.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
   ce11b20..24fb72f  main -> main
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat scripts/cost_tag_check.py
cat fixtures/plan.json
"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
  - Prints which specific resource address(es) are missing the tag.

Run manually: python scripts/cost_tag_check.py fixtures/plan.json
"""
import json
import sys


def check_plan(plan_path: str) -> int:
    """
    Returns an exit code: 0 if every taggable resource being created/changed has
    `landlord_account_id`, non-zero otherwise.
    """
    raise NotImplementedError("Implement this.")


if __name__ == "__main__":
    sys.exit(check_plan(sys.argv[1]))
{
  "format_version": "1.2",
  "resource_changes": [
    {
      "address": "aws_s3_bucket.landlord_media[0]",
      "type": "aws_s3_bucket",
      "name": "landlord_media",
      "change": {
        "actions": ["create"],
        "after": {
          "bucket": "haven-media-la-001",
          "tags": { "landlord_account_id": "la-001" }
        }
      }
    },
    {
      "address": "aws_s3_bucket.listing_media",
      "type": "aws_s3_bucket",
      "name": "listing_media",
      "change": {
        "actions": ["create"],
        "after": {
          "bucket": "haven-listing-media",
          "tags": { "tenant_id": "ten-001" }
        }
      }
    },
    {
      "address": "aws_lambda_function.mls_feed_sync",
      "type": "aws_lambda_function",
      "name": "mls_feed_sync",
      "change": {
        "actions": ["create"],
        "after": {
          "function_name": "mls-feed-sync",
          "tags": {}
        }
      }
    },
    {
      "address": "aws_lambda_function.screening_report_export",
      "type": "aws_lambda_function",
      "name": "screening_report_export",
      "change": {
        "actions": ["update"],
        "after": {
          "function_name": "screening-report-export",
          "tags": { "landlord_account_id": "la-002", "tenant_id": "ten-002" }
        }
      }
    }
  ]
}
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py
1:grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py"""
26:    `landlord_account_id`, non-zero otherwise.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py
1:grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py"""
26:    `landlord_account_id`, non-zero otherwise.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_cost_tag_check.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 0 items / 1 error

========================================================================== ERRORS ==========================================================================
______________________________________________________ ERROR collecting tests/test_cost_tag_check.py _______________________________________________________
.venv/lib/python3.14/site-packages/_pytest/python.py:528: in importtestmodule
    mod = import_path(
.venv/lib/python3.14/site-packages/_pytest/pathlib.py:640: in import_path
    importlib.import_module(module_name)
/usr/lib/python3.14/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<frozen importlib._bootstrap>:1406: in _gcd_import
    ???
<frozen importlib._bootstrap>:1371: in _find_and_load
    ???
<frozen importlib._bootstrap>:1342: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:938: in _load_unlocked
    ???
.venv/lib/python3.14/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_cost_tag_check.py:12: in <module>
    from scripts.cost_tag_check import check_plan
E     File "/home/ubuntu/haven-platform-assessment/scripts/cost_tag_check.py", line 1
E       grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py"""
E               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   SyntaxError: invalid syntax
===================================================================== warnings summary =====================================================================
scripts/cost_tag_check.py:1
  /home/ubuntu/haven-platform-assessment/scripts/cost_tag_check.py:1: SyntaxWarning: "\|" is an invalid escape sequence. Such sequences will not work in the
 future. Did you mean "\\|"? A raw string is also an option.
    grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py"""

<input>:1
<input>:1
<input>:1
<input>:1
  <input>:1: SyntaxWarning: "\|" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\|"? A raw string is also an opti
on.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================= short test summary info ==================================================================
ERROR tests/test_cost_tag_check.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=============================================================== 5 warnings, 1 error in 0.17s ===============================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py
1:grep -n "tenant_id\|landlord_account_id" scripts/cost_tag_check.py"""
26:    `landlord_account_id`, non-zero otherwise.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ sed -i '1d' scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ head -20 scripts/cost_tag_check.py
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
  - Prints which specific resource address(es) are missing the tag.

Run manually: python scripts/cost_tag_check.py fixtures/plan.json
"""
import json
import sys

(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ sed -i '1i"""' scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ head -15 scripts/cost_tag_check.py
"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
  - Prints which specific resource address(es) are missing the tag.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ sed -i '1i"""' scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ """
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan:
> head -15 scripts/cost_tag_check.py
>
>
> ^C
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ head -15 scripts/cost_tag_check.py
"""
"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ head -5 scripts/cost_tag_check.py
"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ python -m py_compile scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ tail -40 scripts/cost_tag_check.py
"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
  - Prints which specific resource address(es) are missing the tag.

Run manually: python scripts/cost_tag_check.py fixtures/plan.json
"""
import json
import sys


def check_plan(plan_path: str) -> int:
    """
    Returns an exit code: 0 if every taggable resource being created/changed has
    `landlord_account_id`, non-zero otherwise.
    """
    raise NotImplementedError("Implement this.")


if __name__ == "__main__":
    sys.exit(check_plan(sys.argv[1]))
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ python -m py_compile scripts/cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ grep -n "REQUIRED_TAG\|landlord_account_id" scripts/cost_tag_check.py
5:Checks Terraform plan resources for the required landlord_account_id tag.
11:REQUIRED_TAG = "landlord_account_id"
17:    0 if every resource being created/changed has landlord_account_id.
38:        if not isinstance(tags, dict) or not tags.get(REQUIRED_TAG):
43:        print(f"Missing required tag '{REQUIRED_TAG}':")
48:    print(f"All resources have the required tag '{REQUIRED_TAG}'.")
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ python scripts/cost_tag_check.py fixtures/plan.json
echo "exit=$?"
Missing required tag 'landlord_account_id':
aws_lambda_function.mls_feed_sync
aws_s3_bucket.listing_media
exit=1
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ echo "=== RUN 1 ==="
python scripts/cost_tag_check.py fixtures/plan.json
echo "exit=$?"

echo "=== RUN 2 ==="
python scripts/cost_tag_check.py fixtures/plan.json
echo "exit=$?"
=== RUN 1 ===
Missing required tag 'landlord_account_id':
aws_lambda_function.mls_feed_sync
aws_s3_bucket.listing_media
exit=1
=== RUN 2 ===
Missing required tag 'landlord_account_id':
aws_lambda_function.mls_feed_sync
aws_s3_bucket.listing_media
exit=1
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_cost_tag_check.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 0 items

================================================================== no tests ran in 0.02s ===================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 4 items

tests/test_access_control.py::test_manager_can_access_report_in_same_landlord_account PASSED                                                         [ 25%]
tests/test_access_control.py::test_manager_cannot_access_another_landlord_account PASSED                                                             [ 50%]
tests/test_access_control.py::test_missing_tenant_denies_access PASSED                                                                               [ 75%]
tests/test_access_control.py::test_missing_property_denies_access PASSED                                                                             [100%]

==================================================================== 4 passed in 0.02s =====================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat tests/test_cost_tag_check.py
"""
Write tests here proving:
  1. Happy path: running the check against fixtures/plan.json correctly flags the resources
     missing `landlord_account_id` (listing_media, mls_feed_sync) and passes the ones that
     have it (landlord_media[0], screening_report_export).
  2. Idempotency: running the check twice against the same plan file produces the same
     result both times, with no duplicated output.

Use a test double / your own in-memory plan dict where you don't need a real file on disk —
you don't need to shell out to the real script for every case.
"""
from scripts.cost_tag_check import check_plan
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano tests/test_cost_tag_check.py
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest tests/test_cost_tag_check.py -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 3 items

tests/test_cost_tag_check.py::test_fixture_plan_flags_missing_landlord_account_tags PASSED                                                           [ 33%]
tests/test_cost_tag_check.py::test_cost_tag_check_is_idempotent PASSED                                                                               [ 66%]
tests/test_cost_tag_check.py::test_resources_without_create_or_update_are_skipped PASSED                                                             [100%]

==================================================================== 3 passed in 0.03s =====================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ pytest -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0 -- /home/ubuntu/haven-platform-assessment/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/haven-platform-assessment
collected 7 items

tests/test_access_control.py::test_manager_can_access_report_in_same_landlord_account PASSED                                                         [ 14%]
tests/test_access_control.py::test_manager_cannot_access_another_landlord_account PASSED                                                             [ 28%]
tests/test_access_control.py::test_missing_tenant_denies_access PASSED                                                                               [ 42%]
tests/test_access_control.py::test_missing_property_denies_access PASSED                                                                             [ 57%]
tests/test_cost_tag_check.py::test_fixture_plan_flags_missing_landlord_account_tags PASSED                                                           [ 71%]
tests/test_cost_tag_check.py::test_cost_tag_check_is_idempotent PASSED                                                                               [ 85%]
tests/test_cost_tag_check.py::test_resources_without_create_or_update_are_skipped PASSED                                                             [100%]

==================================================================== 7 passed in 0.03s =====================================================================
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ nano DESIGN_NOTES.md
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cat DESIGN_NOTES.md
grep -ci idempotency DESIGN_NOTES.md
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
3
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ git add DESIGN_NOTES.md
git commit -m "Add design notes with idempotency key"
git push
[main 5c08585] Add design notes with idempotency key
 1 file changed, 20 insertions(+)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 634 bytes | 634.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/maniyarasansadagopan-crypto/haven-platform-assessment.git
   24fb72f..5c08585  main -> main
(.venv) ubuntu@ip-172-31-2-146:~/haven-platform-assessment$ cd ~/haven-platform-assessment
tmux capture-pane -p -S - > ~/terminal_raw.txt

```
