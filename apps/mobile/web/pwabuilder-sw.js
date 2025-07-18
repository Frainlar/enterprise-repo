self.addEventListener('install', event => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open('offline').then(cache => {
      return cache.match(event.request).then(response => {
        return response || fetch(event.request);
      });
    })
  );
});
