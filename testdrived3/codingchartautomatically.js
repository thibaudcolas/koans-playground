import d3 from 'd3';

export default function(numbers) {
    d3.select('.chart')
        .selectAll('div')
        .data(numbers)
    .enter().append('div')
        .style('width', d => `${d * 10}px`)
        .text(d => d);
}
