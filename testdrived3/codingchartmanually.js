import d3 from 'd3';

export default function() {
    d3.select('.chart')
        .html(`
            <div style="width: 40px;">4</div>
            <div style="width: 80px;">8</div>
            <div style="width: 150px;">15</div>
            <div style="width: 160px;">16</div>
            <div style="width: 230px;">23</div>
            <div style="width: 420px;">42</div>
        `);
}
