import React, { useEffect } from 'react';

const series = [
    'Avengers', 'Fast and furious', 'Iron Man', 'Harry Potter', 'america'
];


export default function Movies() {

    const [movies , setMovies] = useState([]);

    useEffect(() => {
        const promises = series.map(series => {
            fetch(`https://www.omdbapi.com/?s=${encodeURIComponent(series)}&apikey=fed0c24c`)
                .then(res => res.json())
        });

        Promise.all(promises)
            .then(movies => {
                setMovies(movies)
            });
    },[]);

    return movies.map(movie => {
        return <Movie />
    })

    return (
        <div>
            <h1>HI</h1>
        </div>
    );
}