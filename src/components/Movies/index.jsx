import { color } from '@material-ui/system';
import { display } from '@material-ui/system';
import React, { useEffect, useState } from 'react';
import handleOnSubmit , {inputVal} from '../Header';
import api from './api.info';

export default function Movies() {

    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetch(api.test2_api)
            .then(res => res.json())
            .then(data => {
                console.log(data);
                setMovies(data.results);
            });
    }, []);

    console.log(inputVal);

    return ( 
        movies.map((movie) => 
            <div 
                className="movie" 
                key = {movie.id}
            >
                <img 
                    src = {api.image_api + movie.poster_path} 
                    alt = {movie.title}
                />

                <div className="movie-text-section">
                    <h4 className="movie-title">
                        {movie.title}
                    </h4>


                    <h4 
                        className = "movie-rating"
                        // style = {{movie.vote_average > 8} ? {color : green} : {color : yellow}} 
                    >
                        {movie.vote_average}
                        
                        {/* {movie.vote_average > 8 ? {className = "movie-rating-good"} : {className = "movie-rating-poor"}} */}

                    </h4>
                </div>
                    <div className="movie-overview">
                        <h3>{movie.title}</h3>
                        <p>{movie.overview}</p>
                    </div>
            </div>
        )
    );
}