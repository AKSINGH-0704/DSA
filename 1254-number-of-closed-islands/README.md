<h2><a href="https://leetcode.com/problems/number-of-closed-islands">Number of Closed Islands</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a 2D&nbsp;<code>grid</code> consists of <code>0s</code> (land)&nbsp;and <code>1s</code> (water).&nbsp; An <em>island</em> is a maximal 4-directionally connected group of <code><font face="monospace">0</font>s</code> and a <em>closed island</em>&nbsp;is an island <strong>totally</strong>&nbsp;(all left, top, right, bottom) surrounded by <code>1s.</code></p>

<p>Return the number of <em>closed islands</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><img alt="" src="https://assets.leetcode.com/uploads/2026/10/27/sample_3_1610.png" style="width: 250px; height: 157px;" /></p>

<p><strong>Input:</strong> <span class="example-io">grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The grid contains four islands of 0s.</li>
	<li>The island spanning rows 1 to 3 and columns 1 to 4 is surrounded entirely by 1s. It also encloses the water cell at row 2, column 2. It is therefore closed.</li>
	<li>The single 0 at row 3, column 6 has 1s on all four sides, so it is also closed.</li>
	<li>The two remaining islands both lie in column 7, which is on the border of the grid, so neither of them is closed.</li>
	<li>Two islands are closed, shown in gray, so the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><img alt="" src="https://assets.leetcode.com/uploads/2026/10/27/sample_4_1610.png" style="width: 200px; height: 123px;" /></p>

<p><strong>Input:</strong> <span class="example-io">grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The grid contains three islands of 0s.</li>
	<li>The single 0 at row 1, column 2 has 1s above it, below it, to its left and to its right, so it is closed. It is shown in gray.</li>
	<li>The island formed by rows 0 to 2 of column 0 together with row 0, column 1 lies on the border, so it is not closed.</li>
	<li>The island formed by rows 0 to 2 of column 4 together with row 0, column 3 also lies on the border, so it is not closed.</li>
	<li>One island is closed, so the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The grid contains two islands of 0s, one nested inside the other.</li>
	<li>The outer island is the ring of 0s occupying rows 1 to 5 and columns 1 to 5. It is enclosed by the outer border of 1s, so it is closed.</li>
	<li>The inner island is the single 0 at row 3, column 3. It is enclosed by the inner ring of 1s, so it is also closed.</li>
	<li>Both islands are closed, so the answer is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[0].length &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;=1</code></li>
</ul>
