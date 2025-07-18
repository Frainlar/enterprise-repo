import type { Meta, StoryObj } from '@storybook/react';
import { AgentConsole } from './AgentConsole';

const meta: Meta<typeof AgentConsole> = {
  title: 'Organisms/Agent Console',
  component: AgentConsole,
  tags: ['autodocs'],
};
export default meta;
type Story = StoryObj<typeof AgentConsole>;

export const Basic: Story = {};
