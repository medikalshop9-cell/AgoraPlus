// App Theme — AGORA+
// Phase: Frontend Development (Phase 3)
// Colors per docs/frontend_guidelines.md:
//   Primary: Deep Blue | Secondary: White | Accent: Gold | Neutral: Gray
// Typography: Roboto — 22-24px titles, 18px section, 14-16px body, 12px captions

import 'dart:io';
import 'package:flutter/material.dart';

class AppTheme {
 static const Color primary = Color(0xFF0D2E6E); // Deep Blue
 static const Color accent = Color(0xFFC9A84C); // Gold
 static const Color neutral = Color(0xFFF2F2F2); // Light Gray
 
 static ThemeData get lightTheme => ThemeData(
       fontFamily: Platform.isIOS ? null : 'Inter', // 🔥 key fix
       colorScheme: ColorScheme.fromSeed(
         seedColor: primary,
         secondary: accent,
       ),
       scaffoldBackgroundColor: Colors.white,
     );
}
