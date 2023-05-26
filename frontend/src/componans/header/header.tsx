
import React from "react";
import { useTranslation } from "react-i18next";
import "./header.css"

import "./header.css"
const Header = () => {
    const { t, i18n } = useTranslation();
    const changeLanguage = (lng: string) => {
        i18n.changeLanguage(lng);
      };
    
      const placeholder = t("search") || "";

    return (
            <div className="header">
                <div className="upper-header">
                    <div className="container">
                        <div className="left-side">
                            <a href="#" className="logo">VILKA</a>
                            <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg" className="vilka">
                                <path d="M19.4306 30.3284C18.3809 29.817 17.7226 28.9664 17.235 27.9585C16.5877 26.6203 16.3597 25.1983 16.3829 23.7247C16.3888 23.3482 16.4183 23.3705 16.0338 23.3331C15.1531 23.2474 14.2773 23.1255 13.4644 22.7381C12.5393 22.2973 12.0584 21.5577 12.0462 20.5423C12.0272 18.9567 12.04 17.3707 12.0368 15.7849C12.0362 15.5157 12.0197 15.2466 12.0162 14.9773C12.0116 14.629 12.014 14.6281 12.3529 14.628C13.731 14.6278 15.1092 14.6283 16.4873 14.6284C18.466 14.6285 20.4446 14.6283 22.4233 14.6286C22.7283 14.6287 22.7352 14.6297 22.7346 14.937C22.7318 16.3838 22.8086 17.831 22.7365 19.2773C22.6938 20.1347 22.5754 20.9781 22.0729 21.7143C21.5534 22.4755 20.7946 22.8677 19.9372 23.1117C19.5067 23.2343 19.0652 23.2943 18.622 23.3419C18.5048 23.3545 18.4368 23.3861 18.432 23.5173C18.3786 24.9578 18.568 26.3423 19.3651 27.5873C19.4939 27.7886 19.639 27.9772 19.8153 28.1412C20.2712 28.5654 20.7894 28.7244 21.4076 28.5695C23.8723 27.9522 25.7993 26.5826 27.188 24.4571C28.2347 22.8552 28.8157 21.0847 29.0336 19.1949C29.3285 16.6379 28.8964 14.2088 27.6208 11.9618C26.1304 9.33622 23.9426 7.53453 21.0793 6.56207C19.678 6.08615 18.2325 5.89655 16.761 5.98306C14.1867 6.13441 11.8886 7.02506 9.90203 8.67866C7.98748 10.2723 6.70478 12.2794 6.05984 14.6859C5.65929 16.1804 5.55929 17.6972 5.77501 19.2335C6.18102 22.1252 7.48262 24.5387 9.65877 26.4756C10.9057 27.5853 12.3363 28.3858 13.9372 28.8681C14.3827 29.0023 14.7093 29.2263 14.8141 29.7108C14.9668 30.417 14.2796 31.0845 13.582 30.8862C11.3995 30.2661 9.49538 29.1576 7.86179 27.5869C6.22778 26.0158 5.04518 24.1537 4.33389 22.0011C3.76566 20.2814 3.53898 18.5168 3.67158 16.7045C3.82983 14.5417 4.44562 12.5229 5.55585 10.6637C6.847 8.50162 8.60318 6.81165 10.8147 5.59978C11.9834 4.95937 13.2219 4.50505 14.5246 4.23202C16.0183 3.91895 17.5256 3.83615 19.0405 4.04536C23.9602 4.72472 27.5294 7.30956 29.7885 11.7132C30.4142 12.9328 30.7925 14.2428 30.9963 15.5966C31.1987 16.9418 31.1963 18.2895 31.0222 19.6426C30.7357 21.8701 30.022 23.9361 28.7536 25.7943C27.1757 28.1061 25.0406 29.662 22.3425 30.4286C21.6448 30.6268 20.9413 30.7878 20.2086 30.5962C19.947 30.5278 19.6919 30.4476 19.4306 30.3284Z" fill="#D63A3F"/>
                                <path d="M15.4808 12.0571C15.4806 12.5493 15.4743 13.0184 15.4832 13.4873C15.4867 13.6763 15.4212 13.7439 15.2296 13.7401C14.7146 13.7301 14.1992 13.7312 13.6842 13.7398C13.506 13.7428 13.4371 13.6826 13.438 13.502C13.4433 12.4333 13.4413 11.3645 13.4425 10.2957C13.4432 9.67508 14.0886 9.38973 14.6244 9.47189C15.2496 9.56776 15.479 9.8542 15.4796 10.4885C15.48 11.0037 15.4804 11.5189 15.4808 12.0571Z" fill="#D63A3F"/>
                                <path d="M19.309 11.4566C19.309 11.0952 19.307 10.7568 19.3095 10.4185C19.3142 9.78257 19.8049 9.37023 20.4414 9.46475C21.0913 9.56125 21.3359 9.84124 21.3374 10.4951C21.3398 11.4793 21.3362 12.4636 21.3456 13.4477C21.3476 13.6619 21.2893 13.7482 21.0592 13.7409C20.5599 13.725 20.0596 13.7296 19.56 13.7397C19.3688 13.7435 19.3036 13.6755 19.3057 13.4865C19.3133 12.8177 19.3089 12.1486 19.309 11.4566Z" fill="#D63A3F"/>
                            </svg>
                        </div>
                        <div className="right-side">
                           <a href="#" className="ukr" onClick={() => changeLanguage("uk")}>
              UKR
            </a>
            <div className="cross"></div>
            <a href="#" className="eng" onClick={() => changeLanguage("en")}>
              ENG</a>
                        </div>
                    </div>
                </div>

                <div className="down-header">
                    <div className="container">
                        <a href="#" className="catalog-menu">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="icon-catalog-menu">
                                <path d="M4 8H8V4H4V8ZM10 20H14V16H10V20ZM4 20H8V16H4V20ZM4 14H8V10H4V14ZM10 14H14V10H10V14ZM16 4V8H20V4H16ZM10 8H14V4H10V8ZM16 14H20V10H16V14ZM16 20H20V16H16V20Z" fill="white"/>
                            </svg>
                            {t("catalog")}
                        </a>
                        <div className="input-box">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="icon-search">
                                <path d="M15.7549 14.255H14.9649L14.6849 13.985C15.6649 12.845 16.2549 11.365 16.2549 9.755C16.2549 6.165 13.3449 3.255 9.75488 3.255C6.16488 3.255 3.25488 6.165 3.25488 9.755C3.25488 13.345 6.16488 16.255 9.75488 16.255C11.3649 16.255 12.8449 15.665 13.9849 14.685L14.2549 14.965V15.755L19.2549 20.745L20.7449 19.255L15.7549 14.255ZM9.75488 14.255C7.26488 14.255 5.25488 12.245 5.25488 9.755C5.25488 7.265 7.26488 5.255 9.75488 5.255C12.2449 5.255 14.2549 7.265 14.2549 9.755C14.2549 12.245 12.2449 14.255 9.75488 14.255Z" fill="#323030"/>
                            </svg>
                            <input type="text" className="search" placeholder={placeholder}/>                            <a href="#" className="mic-link">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="icon-microphone">
                                    <path d="M12 14.5C13.66 14.5 15 13.16 15 11.5V5.5C15 3.84 13.66 2.5 12 2.5C10.34 2.5 9 3.84 9 5.5V11.5C9 13.16 10.34 14.5 12 14.5ZM11 5.5C11 4.95 11.45 4.5 12 4.5C12.55 4.5 13 4.95 13 5.5V11.5C13 12.05 12.55 12.5 12 12.5C11.45 12.5 11 12.05 11 11.5V5.5ZM17 11.5C17 14.26 14.76 16.5 12 16.5C9.24 16.5 7 14.26 7 11.5H5C5 15.03 7.61 17.93 11 18.42V21.5H13V18.42C16.39 17.93 19 15.03 19 11.5H17Z" fill="#323030"/>
                                </svg>
                            </a>
                            <a href="#" className="search-btn"> {t("search")}</a>
                        </div>
                        <ul className="nav-menu">
                            <li className="nav-item">
                                <a href="#" className="nav-link">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="nav-icon">
                                        <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM7.07 18.28C7.5 17.38 10.12 16.5 12 16.5C13.88 16.5 16.51 17.38 16.93 18.28C15.57 19.36 13.86 20 12 20C10.14 20 8.43 19.36 7.07 18.28ZM18.36 16.83C16.93 15.09 13.46 14.5 12 14.5C10.54 14.5 7.07 15.09 5.64 16.83C4.62 15.49 4 13.82 4 12C4 7.59 7.59 4 12 4C16.41 4 20 7.59 20 12C20 13.82 19.38 15.49 18.36 16.83ZM12 6C10.06 6 8.5 7.56 8.5 9.5C8.5 11.44 10.06 13 12 13C13.94 13 15.5 11.44 15.5 9.5C15.5 7.56 13.94 6 12 6ZM12 11C11.17 11 10.5 10.33 10.5 9.5C10.5 8.67 11.17 8 12 8C12.83 8 13.5 8.67 13.5 9.5C13.5 10.33 12.83 11 12 11Z" fill="white"/>
                                    </svg>
                                    {t("cabinet")}
                                </a>
                            </li>
                            <li className="nav-item">
                                <a href="#" className="nav-link">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M13 8.33C13.85 8.03 14.53 7.35 14.83 6.5H18L15 13.5C15 15.16 16.57 16.5 18.5 16.5C20.43 16.5 22 15.16 22 13.5L19 6.5H21V4.5H14.83C14.42 3.33 13.31 2.5 12 2.5C10.69 2.5 9.58 3.33 9.17 4.5H3V6.5H5L2 13.5C2 15.16 3.57 16.5 5.5 16.5C7.43 16.5 9 15.16 9 13.5L6 6.5H9.17C9.47 7.35 10.15 8.03 11 8.33V19.5H2V21.5H22V19.5H13V8.33ZM20.37 13.5H16.63L18.5 9.14L20.37 13.5ZM7.37 13.5H3.63L5.5 9.14L7.37 13.5ZM12 6.5C11.45 6.5 11 6.05 11 5.5C11 4.95 11.45 4.5 12 4.5C12.55 4.5 13 4.95 13 5.5C13 6.05 12.55 6.5 12 6.5Z" fill="white"/>
                                    </svg>
                                    {t("comparison")}
                                </a>
                            </li>
                            <li className="nav-item">
                                <a href="#" className="nav-link">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M16.5 2.82495C14.76 2.82495 13.09 3.63495 12 4.91495C10.91 3.63495 9.24 2.82495 7.5 2.82495C4.42 2.82495 2 5.24495 2 8.32495C2 12.105 5.4 15.185 10.55 19.865L12 21.175L13.45 19.855C18.6 15.185 22 12.105 22 8.32495C22 5.24495 19.58 2.82495 16.5 2.82495ZM12.1 18.375L12 18.475L11.9 18.375C7.14 14.065 4 11.215 4 8.32495C4 6.32495 5.5 4.82495 7.5 4.82495C9.04 4.82495 10.54 5.81495 11.07 7.18495H12.94C13.46 5.81495 14.96 4.82495 16.5 4.82495C18.5 4.82495 20 6.32495 20 8.32495C20 11.215 16.86 14.065 12.1 18.375Z" fill="white"/>
                                    </svg>
                                    {t("want")}
                                </a>
                            </li>
                            <li className="nav-item">
                                <a href="#" className="nav-link">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M16.5463 13C17.2963 13 17.9563 12.59 18.2963 11.97L21.8763 5.48C22.2463 4.82 21.7663 4 21.0063 4H6.20634L5.26634 2H1.99634V4H3.99634L7.59634 11.59L6.24634 14.03C5.51634 15.37 6.47634 17 7.99634 17H19.9963V15H7.99634L9.09634 13H16.5463ZM7.15634 6H19.3063L16.5463 11H9.52634L7.15634 6ZM7.99634 18C6.89634 18 6.00634 18.9 6.00634 20C6.00634 21.1 6.89634 22 7.99634 22C9.09634 22 9.99634 21.1 9.99634 20C9.99634 18.9 9.09634 18 7.99634 18ZM17.9963 18C16.8963 18 16.0063 18.9 16.0063 20C16.0063 21.1 16.8963 22 17.9963 22C19.0963 22 19.9963 21.1 19.9963 20C19.9963 18.9 19.0963 18 17.9963 18Z" fill="white"/>
                                    </svg>
                                    {t("cart")}
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
    );
};

export default Header;