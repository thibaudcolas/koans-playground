import d3 from 'd3';

export default function(numbers) {
    const widthScale = d3.scale.linear()
        .domain([0, d3.max(numbers)])
        .range([0, 300]);

    d3.select('.chart')
        .selectAll('div')
        .data(numbers)
    .enter().append('div')
        .style('width', d => `${widthScale(d)}px`)
        .text(d => d);
}
