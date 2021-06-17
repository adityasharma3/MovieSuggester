import { MovieTwoTone } from '@material-ui/icons';
import React, { useEffect, useState } from 'react';
import api from './api.info';

export default function Movies() {

    const [movies, setMovies] = useState([]);

    let poster_path = '', title = '';

    useEffect(() => {
        fetch(api.test2_api)
            .then(res => res.json())
            .then(data => {
                console.log(data);
                setMovies(data.results);
            });
    }, []);


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

                    <h4 className = "movie-rating">
                        {movie.vote_average}
                    </h4>
                </div>
            </div>
        )
    );
}