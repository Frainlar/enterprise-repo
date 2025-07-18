import type { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  storybookShots: {
    storybookUrl: './storybook-static',
    breakpoints: [375, 768, 1024]
  },
  generateOnly: false,
  failOnDifference: true
};
export default config;
