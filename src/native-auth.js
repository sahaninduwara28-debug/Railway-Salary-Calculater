// Bundle the Capacitor Firebase Authentication plugin into the WebView.
import { FirebaseAuthentication } from '@capacitor-firebase/authentication';
window.FirebaseAuthentication = FirebaseAuthentication;

// Bundle the native Biometric Authentication plugin.
import { BiometricAuth } from '@aparajita/capacitor-biometric-auth';
window.BiometricAuth = BiometricAuth;
