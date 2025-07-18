import Redis from 'ioredis';

export function createRedisClient(url: string) {
  return new Redis(url);
}

export async function saveDocument(client: Redis, key: string, value: string) {
  await client.set(key, value);
}

export async function loadDocument(client: Redis, key: string): Promise<string | null> {
  return client.get(key);
}
