import 'package:flutter/material.dart';
import 'api/api_client.dart';
import 'pages/home_page.dart';
import 'pages/agent_dashboard_page.dart';
import 'pages/sap_summary_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final apiClient = ApiClient('https://api.example.com');

    return MaterialApp(
      title: 'Enterprise Mobile',
      routes: {
        '/': (context) => const HomePage(),
        '/dashboard': (context) => const AgentDashboardPage(),
        '/sap-summary': (context) => const SapSummaryPage(),
      },
      initialRoute: '/',
    );
  }
}
