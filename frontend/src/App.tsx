import "./componans/reset/reset.css";
import Categories from "./componans/category/categories";
import Header from "./componans/header/header"
import Catalog_slider from "./componans/catalog-slider/catalog-slider"
import CardList from "./componans/cards-list/cardsList";
function App() {
  return (
  <div className="App">
  <Header></Header>
  {/* <Categories></Categories> */}
  <Catalog_slider></Catalog_slider>
  <CardList></CardList>
    </div>);
  
}

export default App;
