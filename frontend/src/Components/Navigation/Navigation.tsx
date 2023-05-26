import React from "react";
import "./navigation.scss";
import CatalogButton from "../CatalogButton/CatalogButton";
import Search from "../Search/Search";
import IconsButton from "../IconsButton/IconsButton";

export default function Navigation() {
  return (
    <div className="navigation">
      <div className="navigation_container">
        <CatalogButton />
        <Search />
        <IconsButton />
      </div>
    </div>
  );
}
