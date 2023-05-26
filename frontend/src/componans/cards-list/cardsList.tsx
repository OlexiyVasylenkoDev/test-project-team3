import React, { useState, useEffect } from 'react';
import "./cardsList.css"
import Card1 from '../card/Card1';
import Card2 from '../card/Card2';
import Card3 from '../card/Card3';
import Card4 from '../card/Card4';
import Card5 from '../card/Card5';
const CardList = () => {
    return (
        <div className='cardslist'>
            <div className="between">
                <div className='container'>
                    <p className='title-of-list'>Популярні товари</p>
                </div>
            </div>
            <div className='container'>
                <ul className='cards-list'>
                    <li className='cards-item'>
                        <Card1></Card1>
                    </li>
                    <li className='cards-item'>
                        <Card3></Card3>
                    </li>
                    <li className='cards-item'>
                        <Card2></Card2>
                    </li>
                    <li className='cards-item'>
                        <Card4></Card4>
                    </li>
                    <li className='cards-item'>
                        <Card5></Card5>
                    </li>
                </ul> 
            </div>
            <div className="between">
                <div className='container'>
                    <p className='title-of-list'>Рекомендовані товари</p>
                </div>
            </div>
            <div className='container'>
                <ul className='cards-list'>
                    <li className='cards-item'>
                        <Card3></Card3>
                    </li>
                    <li className='cards-item'>
                        <Card4></Card4>
                    </li>
                    <li className='cards-item'>
                        <Card1></Card1>
                    </li>
                    <li className='cards-item'>
                        <Card5></Card5>
                    </li>
                    <li className='cards-item'>
                        <Card2></Card2>
                    </li>
                </ul> 
            </div>
            <div className="between">
                <div className='container'>
                    <p className='title-of-list'>Ідеї для подарунку</p>
                </div>
            </div>
            <div className='container'>
                <ul className='cards-list'>
                    <li className='cards-item'>
                        <Card4></Card4>
                    </li>
                    <li className='cards-item'>
                        <Card1></Card1>
                    </li>
                    <li className='cards-item'>
                        <Card5></Card5>
                    </li>
                    <li className='cards-item'>
                        <Card2></Card2>
                    </li>
                    <li className='cards-item'>
                        <Card3></Card3>
                    </li>
                </ul> 
            </div>
            <div className="between"></div>
        </div>

    );
};

export default CardList;
