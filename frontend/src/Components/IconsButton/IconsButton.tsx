import React from "react";
import "./iconsButton.scss";

export default function IconsButton() {
  return (
    <>
      <div className="icons">
        <div className="icons_block">
          <div>
            <img src="../img/cabinet.svg" />
          </div>
          <div className="icons_descr">Кабінет</div>
        </div>
        <div className="icons_block">
          <div>
            <img src="../img/equal.svg" />
          </div>
          <div className="icons_descr">Порівняння</div>
        </div>
        <div className="icons_block">
          <div>
            <img src="../img/favorites.svg" />
          </div>
          <div className="icons_descr">Бажане</div>
        </div>
        <div className="icons_block">
          <div>
            <img src="../img/card.svg" />
          </div>
          <div className="icons_descr">Кошик</div>
        </div>
      </div>
    </>
  );
}
