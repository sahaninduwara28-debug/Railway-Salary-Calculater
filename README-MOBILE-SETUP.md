# Salary Pro Ultimate V3.2 — PWA + Android + iOS starter

This project preserves the supplied V3.2 HTML app as `www/index.html` and adds a Capacitor wrapper plus PWA metadata/offline shell.

## Build on a computer

Requirements: Node.js LTS, Android Studio + Android SDK for Android; macOS + Xcode for iOS.

```bash
npm install
npx cap add android
npx cap add ios       # macOS only
npx cap sync
npx cap open android  # build APK/AAB in Android Studio
npx cap open ios      # archive/sign in Xcode on macOS
```

After changing `www/index.html`, run `npx cap sync` again.

## PWA hosting

Host the contents of `www/` on an HTTPS host (GitHub Pages/Firebase Hosting). Android Chrome supports install; on iPhone use Safari > Share > Add to Home Screen. A production PWA should add properly sized 192x192 and 512x512 PNG icons and update `manifest.webmanifest` before release.

## Important V3.2 checks before public release

- Existing app data is in browser `localStorage`. Capacitor's WebView storage is separate from Chrome/Safari storage. Export a JSON backup before changing app containers; test restore on each platform.
- Firebase Google sign-in currently uses `signInWithPopup`. Popup-based OAuth may not work reliably inside a native WebView. Native Android/iOS release should switch to a supported native OAuth flow (for example Firebase native authentication plugin) and verify authorized domains, SHA fingerprints / iOS URL schemes.
- Test Firestore security rules with authenticated per-user access; never publish permissive rules.
- The current WebAuthn fingerprint/face helper is origin-bound and is not equivalent to native biometric authentication. Rework it to use Capacitor native biometric APIs before claiming native biometric support.
- Check external CDN assets (Tailwind, Chart.js, fonts, Tesseract) and offline behavior on real devices.
- Test file chooser, downloads, print/PDF, calendar import, camera/photo selection, app resume/lock, and backup/restore on Android and iOS.
- iOS build/signing and App Store distribution require macOS/Xcode and Apple signing credentials. Direct IPA installation also requires signing/provisioning; it is not the same as sharing an APK.

## App identity

- App ID: `lk.salarypro.ultimate` (change only before first release if a different permanent identifier is wanted)
- Display name: `Salary Pro Ultimate`
