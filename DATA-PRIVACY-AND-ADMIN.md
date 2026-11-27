# Salary Pro Ultimate — Cloud Data Access Notice

Version: 2026-11-27-v1

When a user accepts Cloud Sync, Salary, Attendance, OT, profile and related app records are uploaded to Firebase Firestore.

The project Developer/Admin account, when allowlisted in Firestore Security Rules, can read those uploaded records. Firebase encryption in transit and at rest does not make this end-to-end encrypted. Do not tell users that a Master Password prevents the authorized Admin from viewing cloud records.

Declining Cloud Sync should leave data on the device. Revoking consent should block future app sync, but does not automatically delete previously uploaded cloud records. A deletion workflow must be handled separately.

Before deployment, replace `REPLACE_WITH_ADMIN_FIREBASE_AUTH_UID` in `firestore.rules` with the intended Firebase Authentication UID. Never use public read/write rules or place service-account credentials in client code.

This bundle is a starting implementation. The current app's automatic and manual sync functions still need to be updated to enforce the consent gate and write the required `privacyConsent` object before these rules can accept uploads.
