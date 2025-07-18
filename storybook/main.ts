import type { StorybookConfig } from '@storybook/nextjs';

const config: StorybookConfig = {
  stories: ['../packages/shared-ui/**/*.stories.@(ts|tsx|js|jsx|mdx)'],
  addons: [
    '@storybook/addon-a11y',
    '@storybook/addon-docs',
    '@storybook/addon-controls'
  ],
  framework: {
    name: '@storybook/nextjs',
    options: {}
  },
  docs: { autodocs: true }
};
export default config;
