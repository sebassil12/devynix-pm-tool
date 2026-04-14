import React from "react";
import BreadcrumbComp from "@/app/(DashboardLayout)/layout/shared/breadcrumb/BreadcrumbComp";
import { Metadata } from "next";

const BCrumb = [
  {
    to: "/",
    title: "Home",
  },
  {
    title: "Product list",
  },
];
export const metadata: Metadata = {
  title: "Product List",
};
const EcomProductList = () => {
  return (
    <>
    </>
  )
}

export default EcomProductList
