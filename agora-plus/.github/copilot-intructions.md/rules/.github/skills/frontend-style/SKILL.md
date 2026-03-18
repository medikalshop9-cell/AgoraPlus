# Frontend Guidelines — AGORA+
Built with Flutter.

## Design Principles
- Simplicity: clean, minimal screens
- Speed: key info within 2 taps maximum
- Consistency: same spacing, buttons, typography across all screens
- Mobile-first: no desktop-style layouts

## Navigation
- Persistent bottom navigation (6 tabs max)
- Tabs: Home, Events, Community, Voting, Members, Profile

## Secondary Navigation
Inside sections, navigation may appear as:

Examples:

Events
 ├ Upcoming
 └ Past
Voting
 ├ Active Elections
 └ Past Elections

## Layout Grid
- Outer margin: 16px
- Section spacing: 24px
- Element spacing: 8–12px

## Typography (Roboto)
- Page Titles: 22–24px
- Section Titles: 18px
- Body Text: 14–16px
- Captions: 12px (minimum)

## Color System
- Primary: Deep Blue (navigation highlights)
- Secondary: White
- Accent: Gold (buttons)
- Neutral: Gray tones (backgrounds)
- Strong contrast required for readability

## Button Design
- Primary (RSVP, Vote, Join Meeting): filled, rounded corners, bold text
- Secondary (Download, Calendar): outlined, transparent background

## Cards
- Event Card: poster, title, date, RSVP button
- Announcement Card: title, preview text, timestamp

## Chat Interface
- User avatar, message bubble, timestamp
- Sent: primary color | Received: neutral gray
- Pinned messages at top

## Voting Interface
- Position title, candidate list, vote button, deadline indicator
- Confirmation dialog before submit

## Member Directory Interface
Members tab includes:

Search bar
Admin section
Member list
Each member appears in a profile card:

Photo
Name
Major
Year

## Loading States
- Spinner or skeleton placeholders; no blank screens

## Error States
- Clear, actionable messages (Network error / Try again / Event full)

## Accessibility
- High color contrast
- Touch targets minimum 44px
- Readable fonts, clear icons

## Performance
Frontend must be optimized for speed.
- Lazy load images
- Cache frequently used data
- Minimize animations and network calls
Mobile performance is critical.

## Animation Guidelines
Animations should remain subtle and purposeful.

Examples:
Screen transitions
Button feedback
Notification appearance
Avoid excessive animations that slow the app

Feature
Flutter Property / Widget
Page Swipe
CupertinoPageRoute
List Bounce
BouncingScrollPhysics()
Loading
CupertinoActivityIndicator()
Natural Feel
Curves.easeInOutQuart
Glass Effect
BackdropFilter
Skeleton Loading
Skeletonizer
Hero Transition
Hero
Touch Feedback
InkWell / GestureDetector
Haptic Feedback
HapticFeedback.lightImpact()
Smooth Container Animation
AnimatedContainer
Fade Page Transition
FadeTransition
# Slightly expanded
Feature                     Flutter Property / Widget
Page Swipe                  CupertinoPageRoute
List Bounce                 BouncingScrollPhysics()
Loading                     CupertinoActivityIndicator()
Natural Feel                Curves.easeInOutQuart
Glass Effect                BackdropFilter
Skeleton Loading            Skeletonizer
Hero Transition             Hero
Touch Feedback              InkWell
Haptic Feedback             HapticFeedback.lightImpact()
Smooth Animation            AnimatedContainer
Page Fade Transition        FadeTransition
