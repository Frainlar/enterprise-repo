import 'package:flutter/material.dart';

class SapSummaryPage extends StatelessWidget {
  const SapSummaryPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('SAP Summary')),
      body: const Center(child: Text('High level SAP metrics here.')),
    );
  }
}
