import d3 from 'd3';

export default function() {
    d3.select('body')
        .style('background-color', 'yellow')
    .append('h1')
        .attr('class', 'chart-title')
        .html('D3 bar chart');
}
