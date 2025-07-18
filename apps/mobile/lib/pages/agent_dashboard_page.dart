import 'package:flutter/material.dart';

class AgentDashboardPage extends StatelessWidget {
  const AgentDashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Agent Dashboard')),
      body: const Center(child: Text('Agent stats and controls go here.')),
    );
  }
}
