# Salary Pro Ultimate V3.2 — Android phone-only workflow

## What this repository provides
- PWA files in `www/` for hosting on GitHub Pages.
- GitHub Actions workflow to build an Android **debug APK** and attach it as a workflow artifact.
- GitHub Actions workflow to build an **unsigned iOS Simulator app** on Apple's macOS runner. This is for testing only and cannot be installed on a physical iPhone.

## Upload using only an Android phone
1. Download and extract this ZIP using your phone's Files app.
2. Open GitHub in Chrome and sign in.
3. Create/open the repository you use for Salary Pro.
4. Upload the *contents* of the `salary-pro-v3-mobile` folder to the repository root (make sure `.github/workflows/` is included; enable “show hidden files” if your file picker hides `.github`).
5. Commit to the `main` branch.
6. In GitHub, open **Actions**. Run **Build Android APK** using **Run workflow** (or wait for a push-triggered run).
7. Open the completed run, find **Artifacts**, and download `Salary-Pro-Ultimate-V3.2-Android-debug`. Extract it and install `app-debug.apk`. Android may ask you to allow installs from that browser/files app.

## Publish the PWA
1. In repository **Settings → Pages**, set the source to **GitHub Actions**.
2. Run **Deploy Salary Pro PWA to GitHub Pages** in Actions.
3. Open the published Pages URL in Chrome and use **Install app / Add to Home screen**.
4. On iPhone, open the URL in Safari and choose **Share → Add to Home Screen**.

## iOS reality check
The iOS workflow builds a simulator `.app` only. A physical iPhone IPA requires Apple signing assets (Apple Developer membership, distribution certificate, provisioning profile, and bundle ID setup) and a signed archive/export workflow. This cannot be bypassed by using an Android phone alone. The PWA can still be added to an iPhone Home Screen without an App Store IPA.

## Before using real payroll data
- Export a JSON backup from the existing app before changing browser/app containers.
- Test restore into the new install before deleting the old app or browser data.
- Review Firebase Authentication and Firestore security rules; never use public read/write rules.
- Google popup sign-in and the current WebAuthn helper are not guaranteed to work in native Capacitor WebViews. Native OAuth and native biometric integration remain follow-up engineering tasks.
- Verify salary calculations, overtime and the 45-day leave policy with test records before relying on payroll output.
