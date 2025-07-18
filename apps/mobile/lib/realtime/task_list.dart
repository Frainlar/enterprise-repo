import 'package:redis/redis.dart';

class TaskListService {
  final Command _command;

  TaskListService(String host, int port)
      : _command = Command()..connect(host, port);

  Future<List<String>> getTasks() async {
    final result = await _command.send_object(['LRANGE', 'tasks', '0', '-1']);
    return (result as List).cast<String>();
  }

  Future<void> addTask(String task) async {
    await _command.send_object(['RPUSH', 'tasks', task]);
  }
}
