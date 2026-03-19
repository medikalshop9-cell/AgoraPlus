// AGORA+ — Root app widget
// Phase: Frontend Development (Phase 3)
// Sets global theme and handles auth-based routing

import 'package:flutter/material.dart';
import 'theme/app_theme.dart';
import 'screens/auth/login_screen.dart';
import 'navigation/bottom_nav.dart';

class AgoraApp extends StatelessWidget {
 const AgoraApp({super.key});
 
 @override
 Widget build(BuildContext context) {
   return MaterialApp(
     title: 'AGORA+',
     theme: AppTheme.lightTheme,
     home: const LoginScreen(), // later replace with auth check
   );
 }
}
