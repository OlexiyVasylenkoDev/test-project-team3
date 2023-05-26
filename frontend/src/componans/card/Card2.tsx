import "./Card.css";
import photo2 from "../../img/photo2.jpg"
import { useTranslation } from "react-i18next";
const Card2 = () => {
  
  const { t } = useTranslation();

  return (
    <div className="card">
        <span className="top-seller">{t ("top")}</span>
        <ul className="icon-upper-list">
          <li className="icon-upper-item">
            <a href="" className="icon-upper-link">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M16.5 2.82495C14.76 2.82495 13.09 3.63495 12 4.91495C10.91 3.63495 9.24 2.82495 7.5 2.82495C4.42 2.82495 2 5.24495 2 8.32495C2 12.105 5.4 15.185 10.55 19.865L12 21.175L13.45 19.855C18.6 15.185 22 12.105 22 8.32495C22 5.24495 19.58 2.82495 16.5 2.82495ZM12.1 18.375L12 18.475L11.9 18.375C7.14 14.065 4 11.215 4 8.32495C4 6.32495 5.5 4.82495 7.5 4.82495C9.04 4.82495 10.54 5.81495 11.07 7.18495H12.94C13.46 5.81495 14.96 4.82495 16.5 4.82495C18.5 4.82495 20 6.32495 20 8.32495C20 11.215 16.86 14.065 12.1 18.375Z" fill="black"/>
              </svg>
            </a>
          </li>
          <li className="icon-upper-item">
            <a href="" className="icon-upper-link">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13 8.33C13.85 8.03 14.53 7.35 14.83 6.5H18L15 13.5C15 15.16 16.57 16.5 18.5 16.5C20.43 16.5 22 15.16 22 13.5L19 6.5H21V4.5H14.83C14.42 3.33 13.31 2.5 12 2.5C10.69 2.5 9.58 3.33 9.17 4.5H3V6.5H5L2 13.5C2 15.16 3.57 16.5 5.5 16.5C7.43 16.5 9 15.16 9 13.5L6 6.5H9.17C9.47 7.35 10.15 8.03 11 8.33V19.5H2V21.5H22V19.5H13V8.33ZM20.37 13.5H16.63L18.5 9.14L20.37 13.5ZM7.37 13.5H3.63L5.5 9.14L7.37 13.5ZM12 6.5C11.45 6.5 11 6.05 11 5.5C11 4.95 11.45 4.5 12 4.5C12.55 4.5 13 4.95 13 5.5C13 6.05 12.55 6.5 12 6.5Z" fill="black"/>
              </svg>
            </a>
          </li>
        </ul>
        <img src={photo2} className="card-photo" alt="" />
        <p className="card-info">{t ("cardInfo")}</p>
        <div className="rat-com">
          <ul className="rating-list">
            <li className="rating-item">
              <a href="">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 9.74L14.81 9.12L12 2.5L9.19 9.13L2 9.74L7.46 14.47L5.82 21.5L12 17.77L18.18 21.5L16.55 14.47L22 9.74ZM12 15.9L8.24 18.17L9.24 13.89L5.92 11.01L10.3 10.63L12 6.6L13.71 10.64L18.09 11.02L14.77 13.9L15.77 18.18L12 15.9Z" fill="black"/>
                </svg>
              </a>
            </li>
            <li className="rating-item">
              <a href="">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 9.74L14.81 9.12L12 2.5L9.19 9.13L2 9.74L7.46 14.47L5.82 21.5L12 17.77L18.18 21.5L16.55 14.47L22 9.74ZM12 15.9L8.24 18.17L9.24 13.89L5.92 11.01L10.3 10.63L12 6.6L13.71 10.64L18.09 11.02L14.77 13.9L15.77 18.18L12 15.9Z" fill="black"/>
                </svg>
              </a>
            </li>
            <li className="rating-item">
              <a href="">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 9.74L14.81 9.12L12 2.5L9.19 9.13L2 9.74L7.46 14.47L5.82 21.5L12 17.77L18.18 21.5L16.55 14.47L22 9.74ZM12 15.9L8.24 18.17L9.24 13.89L5.92 11.01L10.3 10.63L12 6.6L13.71 10.64L18.09 11.02L14.77 13.9L15.77 18.18L12 15.9Z" fill="black"/>
                </svg>
              </a>
            </li>
            <li className="rating-item">
              <a href="">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 9.74L14.81 9.12L12 2.5L9.19 9.13L2 9.74L7.46 14.47L5.82 21.5L12 17.77L18.18 21.5L16.55 14.47L22 9.74ZM12 15.9L8.24 18.17L9.24 13.89L5.92 11.01L10.3 10.63L12 6.6L13.71 10.64L18.09 11.02L14.77 13.9L15.77 18.18L12 15.9Z" fill="black"/>
                </svg>
              </a>
            </li>
            <li className="rating-item">
              <a href="">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 9.74L14.81 9.12L12 2.5L9.19 9.13L2 9.74L7.46 14.47L5.82 21.5L12 17.77L18.18 21.5L16.55 14.47L22 9.74ZM12 15.9L8.24 18.17L9.24 13.89L5.92 11.01L10.3 10.63L12 6.6L13.71 10.64L18.09 11.02L14.77 13.9L15.77 18.18L12 15.9Z" fill="black"/>
                </svg>
              </a>
            </li>
          </ul>
          <div className="comments">
            <a href="" className="comments-link">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.82698 7.13803L5.71799 7.59202L4.82698 7.13803ZM5.2682 18.7318L5.9753 19.4389L5.97531 19.4389L5.2682 18.7318ZM17.862 16.173L17.408 15.282H17.408L17.862 16.173ZM19.173 14.862L18.282 14.408V14.408L19.173 14.862ZM19.173 7.13803L18.282 7.59202V7.59202L19.173 7.13803ZM17.862 5.82698L18.316 4.93597V4.93597L17.862 5.82698ZM6.13803 5.82698L6.59202 6.71799L6.13803 5.82698ZM7.20711 16.7929L7.91421 17.5L7.20711 16.7929ZM5.5 10.3C5.5 9.44342 5.50078 8.86113 5.53755 8.41104C5.57337 7.97262 5.6383 7.74842 5.71799 7.59202L3.93597 6.68404C3.68868 7.16937 3.59012 7.68608 3.54419 8.24817C3.49922 8.7986 3.5 9.47642 3.5 10.3H5.5ZM5.5 11.5V10.3H3.5V11.5H5.5ZM3.5 11.5V16.5H5.5V11.5H3.5ZM3.5 16.5V18.4136H5.5V16.5H3.5ZM3.5 18.4136C3.5 19.7054 5.06186 20.3524 5.9753 19.4389L4.56109 18.0247C4.90757 17.6782 5.5 17.9236 5.5 18.4136H3.5ZM5.97531 19.4389L7.91421 17.5L6.5 16.0858L4.56109 18.0247L5.97531 19.4389ZM14.7 15.5H7.91421V17.5H14.7V15.5ZM17.408 15.282C17.2516 15.3617 17.0274 15.4266 16.589 15.4624C16.1389 15.4992 15.5566 15.5 14.7 15.5V17.5C15.5236 17.5 16.2014 17.5008 16.7518 17.4558C17.3139 17.4099 17.8306 17.3113 18.316 17.064L17.408 15.282ZM18.282 14.408C18.0903 14.7843 17.7843 15.0903 17.408 15.282L18.316 17.064C19.0686 16.6805 19.6805 16.0686 20.064 15.316L18.282 14.408ZM18.5 11.7C18.5 12.5566 18.4992 13.1389 18.4624 13.589C18.4266 14.0274 18.3617 14.2516 18.282 14.408L20.064 15.316C20.3113 14.8306 20.4099 14.3139 20.4558 13.7518C20.5008 13.2014 20.5 12.5236 20.5 11.7H18.5ZM18.5 10.3V11.7H20.5V10.3H18.5ZM18.282 7.59202C18.3617 7.74842 18.4266 7.97262 18.4624 8.41104C18.4992 8.86113 18.5 9.44342 18.5 10.3H20.5C20.5 9.47642 20.5008 8.7986 20.4558 8.24817C20.4099 7.68608 20.3113 7.16937 20.064 6.68404L18.282 7.59202ZM17.408 6.71799C17.7843 6.90973 18.0903 7.2157 18.282 7.59202L20.064 6.68404C19.6805 5.93139 19.0686 5.31947 18.316 4.93597L17.408 6.71799ZM14.7 6.5C15.5566 6.5 16.1389 6.50078 16.589 6.53755C17.0274 6.57337 17.2516 6.6383 17.408 6.71799L18.316 4.93597C17.8306 4.68868 17.3139 4.59012 16.7518 4.54419C16.2014 4.49922 15.5236 4.5 14.7 4.5V6.5ZM9.3 6.5H14.7V4.5H9.3V6.5ZM6.59202 6.71799C6.74842 6.6383 6.97262 6.57337 7.41104 6.53755C7.86113 6.50078 8.44342 6.5 9.3 6.5V4.5C8.47642 4.5 7.7986 4.49922 7.24817 4.54419C6.68608 4.59012 6.16937 4.68868 5.68404 4.93597L6.59202 6.71799ZM5.71799 7.59202C5.90973 7.21569 6.21569 6.90973 6.59202 6.71799L5.68404 4.93597C4.93139 5.31947 4.31947 5.93139 3.93597 6.68404L5.71799 7.59202ZM7.91421 17.5H7.91421V15.5C7.38378 15.5 6.87507 15.7107 6.5 16.0858L7.91421 17.5Z" fill="black"/>
                <path d="M8.5 9.5L15.5 9.5" stroke="black" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M8.5 12.5L13.5 12.5" stroke="black" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <p className="value-of-comments">38</p>
            </a>
          </div>
        </div>
        <div className="prices">
          <p className="old-price">2500 ₴</p>
          <p className="new-price">2300 ₴</p>
        </div>
        <a href="" className="btn-buy">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="icon-tray">
            <path d="M16.5463 13C17.2963 13 17.9563 12.59 18.2963 11.97L21.8763 5.48C22.2463 4.82 21.7663 4 21.0063 4H6.20634L5.26634 2H1.99634V4H3.99634L7.59634 11.59L6.24634 14.03C5.51634 15.37 6.47634 17 7.99634 17H19.9963V15H7.99634L9.09634 13H16.5463ZM7.15634 6H19.3063L16.5463 11H9.52634L7.15634 6ZM7.99634 18C6.89634 18 6.00634 18.9 6.00634 20C6.00634 21.1 6.89634 22 7.99634 22C9.09634 22 9.99634 21.1 9.99634 20C9.99634 18.9 9.09634 18 7.99634 18ZM17.9963 18C16.8963 18 16.0063 18.9 16.0063 20C16.0063 21.1 16.8963 22 17.9963 22C19.0963 22 19.9963 21.1 19.9963 20C19.9963 18.9 19.0963 18 17.9963 18Z" fill="black"/>
          </svg>
        </a>
    </div>
  );
};

export default Card2;