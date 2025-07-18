import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import VitePWA from '@vite-pwa/astro';

export default defineConfig({
  site: 'https://example.com',
  integrations: [mdx(), tailwind(), sitemap(), VitePWA()],
});
