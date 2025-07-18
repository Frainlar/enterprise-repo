import { ReactNode } from 'react';

export interface CardProps {
  title: string;
  children: ReactNode;
}

export const Card = ({ title, children }: CardProps) => (
  <div className="border rounded shadow p-4 bg-white">
    <h3 className="font-bold mb-2">{title}</h3>
    <div>{children}</div>
  </div>
);
