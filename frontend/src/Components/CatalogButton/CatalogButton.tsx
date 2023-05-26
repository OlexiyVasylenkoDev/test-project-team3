import React from "react";
import "./catalogButton.scss";

export default function CatalogButton() {
  return (
    <>
      <div className="catalog_btn">
        <div>
          <img src="../img/catalog.svg" alt="img" />
        </div>
        <div>Каталог товарів</div>
      </div>
    </>
  );
}
