SALARY PRO ULTIMATE V3.4 — CLOUD CONSENT UPDATE

මෙම පැකේජයේ:
1. index.html — ඊයේ සකස් කළ V3.3 index(8).html මත පදනම්ව සකස් කළ V3.4.
2. firestore.rules — Admin UID සහ Consent අවශ්‍ය කරන Firestore rules.

යෙදූ වෙනස්කම්:
- පෙර තිබූ Salary, Attendance, OT, Paysheet, Profile, PIN/Biometric, OTP setup UI, Master Password/Encryption setup UI, Settings සහ Sync Center පවත්වා ඇත.
- Sync Center එකට පැහැදිලි Cloud Data Privacy & Consent කොටසක් එක් කර ඇත.
- Cloud වෙත Salary, Attendance, OT, Paysheet, Profile සහ app data යන දත්ත යන බවත් Developer/Admin හට cloud records බැලිය හැකි බවත් පරිශීලකයාට පැහැදිලි කරයි.
- පරිශීලකයා checkbox එක තෝරා “I Agree & Enable Cloud Sync” එබූ පසු පමණක් cloud sync සක්‍රිය වේ.
- Auto Sync, Manual Sync, Cloud restore සහ sign-in පසු sync consent නැතිනම් අවහිර වේ.
- Consent metadata cloud document එකට ලියයි. Firestore rules එය අනිවාර්ය කරයි.
- Revoke Cloud Consent කිරීමෙන් ඉදිරි sync නවතී. දැනටමත් cloud වෙත upload කළ දත්ත ස්වයංක්‍රීයව මැකෙන්නේ නැත.
- Local-only app භාවිතය දිගටම කළ හැකිය.

වැදගත් සීමාවන්:
- OTP methods (Authenticator / Email / SMS) සඳහා UI සහ setup status පමණි. සැබෑ OTP verification backend තවම සකසා නැත.
- Master Password / AES-256-GCM encryption සඳහා setup UI පමණි. දත්ත දැනට encrypted නොවේ. Master Password එකෙන් Admin ට cloud data බැලීම වළක්වන්නේ නැත.
- Firestore Rules publish කරන තුරු ඒවා ක්‍රියාත්මක නොවේ.

GitHub Mobile මඟින්:
1. Repository එකේ www/index.html ගොනුව replace කරන්න (මෙහි index.html එක www/index.html ලෙස upload කරන්න).
2. Repository root එකේ firestore.rules replace කරන්න.
3. Commit changes කරන්න.

Firebase Console මඟින් Rules publish කිරීම:
1. Firebase Console > railway-salary-calculato-1fd86 project එක විවෘත කරන්න.
2. Build > Firestore Database > Rules වෙත යන්න.
3. මෙම පැකේජයේ firestore.rules ගොනුවේ සම්පූර්ණ content එක Rules editor එකට paste කරන්න.
4. Publish ඔබන්න.

Admin UID:
1X8eXTwV5Aa1JX8EzgOYdbF7Gpr2

මෙම update එකෙන් GitHub හෝ Firebase වෙත ස්වයංක්‍රීයව upload/commit/publish කර නැත.
