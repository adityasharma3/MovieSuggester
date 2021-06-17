import './App.scss';
import Header from './components/Header';
import Movies from './components/Movies';

function App() {
	return (
		<div className="App">
			<Header />
			<div className="movie-showcase">
				<Movies />
			</div>
		</div>
	);
}

export default App;
