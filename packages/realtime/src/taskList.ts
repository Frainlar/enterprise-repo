import { TinyliciousClient } from '@fluidframework/tinylicious-client';
import { SharedMap } from 'fluid-framework';

export async function getTaskListContainer(id: string) {
  const client = new TinyliciousClient();
  const schema = { initialObjects: { tasks: SharedMap } };
  let container;
  let containerId = id;
  try {
    container = await client.getContainer(id, schema);
  } catch {
    container = await client.createContainer(schema);
    containerId = await container.attach();
  }
  return { id: containerId, tasks: container.initialObjects.tasks as SharedMap };
}
