import React from "react";
import "./catalogItem.scss";

interface CatalogItemProps {
  img: string;
  title: string;
}

export default function CatalogItem(props: CatalogItemProps) {
  return (
    <div className="item_wrapper">
      <div className="icons">
        <img src={props.img} />
      </div>
      <div className="title">{props.title}</div>
      <div className="more">
        <img src="../img/catalog/more.svg" />
      </div>
    </div>
  );
}
