import {
  IconPoint,
  IconAlertCircle,
  IconSettings,
} from '@tabler/icons-react';
import { uniqueId } from 'lodash';

const Menuitems = [
  {
    id: uniqueId(),
    title: 'Apps',
    icon: 'solar:widget-line-duotone',
    href: '',
    children: [
      {
        id: uniqueId(),
        title: "Contacts",
        icon: 'solar:phone-line-duotone',
        href: "/apps/contacts",
      },
      {
        id: uniqueId(),
        title: "Chats",
        icon: 'solar:chat-round-line-line-duotone',
        href: "/apps/chats",
      },
      {
        id: uniqueId(),
        title: "Notes",
        icon: 'solar:document-text-line-duotone',
        href: "/apps/notes",
      },
      {
        id: uniqueId(),
        title: "Calendar",
        icon: 'solar:calendar-mark-line-duotone',
        href: "/apps/calendar",
      },
      {
        id: uniqueId(),
        title: "Email",
        icon: 'solar:letter-line-duotone',
        href: "/apps/email",
      },
      {
        id: uniqueId(),
        title: "Tickets",
        icon: 'solar:ticker-star-outline',
        href: "/apps/tickets",
      },
      {
        id: uniqueId(),
        title: "Kanban",
        icon: 'solar:notebook-linear',
        href: "/apps/kanban",
      },
      {
        id: uniqueId(),
        title: 'User Profile',
        icon: 'solar:shield-user-outline',
        href: '',
        children: [
          {
            id: uniqueId(),
            title: 'Profile',
            icon: IconPoint,
            href: '/apps/user-profile/profile',
          },
          {
            id: uniqueId(),
            title: 'Followers',
            icon: IconPoint,
            href: '/apps/user-profile/followers',
          },
          {
            id: uniqueId(),
            title: 'Friends',
            icon: IconPoint,
            href: '/apps/user-profile/friends',
          },
          {
            id: uniqueId(),
            title: 'Gallery',
            icon: IconPoint,
            href: '/apps/user-profile/gallery',
          },
        ],
      },
      {
        id: uniqueId(),
        title: 'Ecommerce',
        icon: 'solar:document-text-line-duotone',
        href: '',
        children: [
          {
            id: uniqueId(),
            title: 'List',
            icon: IconPoint,
            href: '/apps/ecommerce/list',
          },
        ],
      },
    ],
  },
];
export default Menuitems;