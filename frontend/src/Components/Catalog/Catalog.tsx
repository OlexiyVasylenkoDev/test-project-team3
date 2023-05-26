import React, { useEffect, useState } from "react";
import CatalogItem from "../CatalogItem/CatalogItem";
import axios from "axios";

interface ICatalog {
  title: string;
}

const CatalogArr = [
  {
    img: "../img/catalog/phoneIcon.svg",
    // title: "Смартфони та телефони",
  },
  {
    img: "../img/catalog/tvIcon.svg",
    // title: "Телевізори і аудіотехніка",
  },
  {
    img: "../img/catalog/laptopIcon.svg",
    // title: "Ноутбуки, ПК, Планшети",
  },
  {
    img: "../img/catalog/healthIcon.svg",
    // title: "Краса та здоров'я",
  },
  {
    img: "../img/catalog/sportIcon.svg",
    // title: "Спорт і туризм",
  },
  {
    img: "../img/catalog/dishIcon.svg",
    // title: "Посуд",
  },
  {
    img: "../img/catalog/carIcon.svg",
    // title: "Автотовари",
  },
  {
    img: "../img/catalog/houseIcon.svg",
    // title: "Товари для саду, городу",
  },
  {
    img: "../img/catalog/kidsIcon.svg",
    // title: "Товари для дітей",
  },

  {
    img: "../img/catalog/zooIcon.svg",
    // title: "Зоотовари",
  },
];

export default function Catalog() {
  const [catalog, setCatalog] = useState<ICatalog[]>([]);

  useEffect(() => {
    fetchCategory();
  }, []);

  async function fetchCategory() {
    try {
      const response = await axios.get(
        "https://ffef-188-130-178-216.ngrok-free.app/api/v1/category",
        {
          headers: {
            "ngrok-skip-browser-warning": "69420",
          },
        }
      );
      setCatalog(response.data);
    } catch (e) {
      console.log(e);
    }
  }

  catalog.map((el) => el.title);
  catalog.splice(0, 22);
  console.log(catalog);

  const mergedCatalog = catalog.map((item, index) => {
    return {
      ...item,
      ...CatalogArr[index],
    };
  });

  console.log(mergedCatalog);
  return (
    <div style={{ paddingTop: "24px", paddingLeft: "72px" }}>
      {mergedCatalog.map((el) => (
        <CatalogItem title={el.title} img={el.img} />
      ))}
    </div>
  );
}
