import prisma from './index';

async function main() {
  await prisma.user.create({
    data: {
      email: 'alice@example.com',
      name: 'Alice',
      orders: {
        create: {
          orderNumber: 'SO-1'
        }
      }
    }
  });
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
