import d3 from 'd3';

export default function() {
    const title = d3.select('body').append('h1');

    title.html('D3 bar chart');
}
