import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiClient {
  final String baseUrl;
  const ApiClient(this.baseUrl);

  Future<http.Response> get(String path) {
    final uri = Uri.parse('$baseUrl$path');
    return http.get(uri);
  }

  Future<http.Response> post(String path, Map<String, dynamic> data) {
    final uri = Uri.parse('$baseUrl$path');
    return http.post(uri, body: jsonEncode(data), headers: {'Content-Type': 'application/json'});
  }
}
