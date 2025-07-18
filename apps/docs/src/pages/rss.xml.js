import rss from '@astrojs/rss';

export async function GET() {
  const posts = import.meta.glob('../content/docs/*.mdx', { eager: true });
  const items = Object.entries(posts).map(([path, mod]) => ({
    title: mod.frontmatter.title,
    link: '/docs/' + path.split('/').pop().replace('.mdx','') + '/',
  }));
  return rss({
    title: 'Docs RSS',
    description: 'Enterprise docs updates',
    site: 'https://example.com',
    items,
  });
}
