import "./Card.scss";

export const Card: React.FC = () => {
  
  return (
    <div className="card ">
      <div className="card__top">
      <span className="card__top__title">топ продаж</span>

      </div>
      <div className="card__labels">
       
          <img className="card__labels__like" src="./img/like.svg" alt="like" />
          <img className="card__labels__scales" src="./img/scales.svg" alt="scales" />
  
      </div>

      <img className="card__photo" src="testCard.png" alt="card photo" />

      <div className="card__info">
        <h3 className="card__info__name">Набір тарілок для кухні Gravis</h3>
        <ul className="card__info__rating">
          <li className="card__info__rating__stars">
            <img className="star" src="./img/star.svg" alt="star" />
          </li>
          <li className="card__info__rating__stars">
            <img className="star" src="./img/star.svg" alt="star" />
          </li>
          <li className="card__info__rating__stars">
            <img className="star" src="./img/star.svg" alt="star" />
          </li>
          <li className="card__info__rating__stars">
            <img className="star" src="./img/star.svg" alt="star" />
          </li>
          <li className="card__info__rating__stars">
            <img className="star" src="./img/star.svg" alt="star" />
          </li>          
        </ul>

        <div className="card__info__message">
            <img className="card__info__message__label" src="./img/massage.svg" alt="massage" />
          <span className="card__info__message__number"> 38</span>

          </div>

        <div className="card__info__price">
        <h3 className="card__info__price__active">1200 ₴</h3>
          <span className="card__info__price__prev">1400 ₴</span>
        </div>

        <button  className="card__info__basket">
          <img src="./img/basket.svg" alt="basket" />
        </button>
      </div>
    </div>
  );
};

export default Card;