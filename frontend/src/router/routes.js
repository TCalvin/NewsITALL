import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";

// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";

// Admin pages
import Dashboard from "@/pages/Dashboard.vue";
import Profile from "@/pages/Profile.vue";
import Discover from "@/pages/Discover.vue";
import Trending from "@/pages/Trending.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "dashboard",
        component: Dashboard,
        props: true
      },
      {
        path: "profile",
        name: "profile",
        component: Profile,
        props: true
      },
      {
        path: "discover",
        name: "discover",
        component: Discover,
        props: true
      },
      {
        path: "trending",
        name: "trending",
        component: Trending,
        props: true
      }
    ],
    props: true
  },
  { path: "*", component: NotFound }
];

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
