[Changelog](https://freemius.com/changelog/) / Fixes to the sales charts in the Developer Dashboard

We noticed that we had two issues with the sales charts in our Developer Dashboard.

### Fixed charts showing future data points

If today’s date was selected as the ‘End Date’ with an ‘Hourly’ resolution, then the charts were showing future hours.

[![Clamping chart dates to current UTC time - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/01/clamping-chart-dates-to-current-utc-time-1024x798.png)](https://freemius.com/blog/wp-content/uploads/2024/01/clamping-chart-dates-to-current-utc-time.png)

As you can see – after the fix – the charts will show until the current GMT hour from now on.

### Fixes in the trial chart

We noticed that we’ve been incorrectly showing ‘Trial cancellation count’ on the ‘Trial cancellation volume’ chart. We’ve fixed this typo.

[![Trial cancellation charts - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/01/trial-cancellation-charts-1024x679.png)](https://freemius.com/blog/wp-content/uploads/2024/01/trial-cancellation-charts.png)

Additionally, we’ve also added the missing ‘Trial cancellation count’ chart to the page.