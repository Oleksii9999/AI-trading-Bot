import numpy as np
import pytest

from jesse.config import config, reset_config
from jesse.store import store


def set_up():
    """

    """
    reset_config()
    config['app']['considering_candles'] = [('Sandbox', 'BTCUSD')]
    store.reset()
    store.orderbooks.init_storage()


def test_add_orderbook_and_orderbook_getters():
    set_up()

    asks = [[9188.76, 52.66], [9189.68, 27.58], [9190.6, 29.36], [9191.52, 47.02], [9192.44, 31.44], [9193.36, 37.89],
            [9194.28, 44.37], [9195.2, 33.84], [9196.12, 26.23], [9197.04, 27.38], [9197.96, 51.1], [9198.88, 56.8],
            [9199.8, 52.01], [9200.72, 46.82], [9201.64, 58.11], [9220.0, 7.579], [9221.45, 1.0], [9232.71, 0.573],
            [9234.15, 0.595], [9236.9, 0.55], [9237.22, 0.573], [9237.92, 0.555], [9238.13, 0.562], [9238.52, 0.546],
            [9238.7, 0.557], [9239.0, 50.0], [9239.42, 0.546], [9240.59, 0.571], [9241.0, 1.0], [9243.0, 24.165],
            [9255.0, 4.0], [9256.66, 0.005], [9274.0, 95.479], [9279.52, 0.129], [9280.0, 0.05], [9300.0, 222.311],
            [9312.0, 4.336], [9330.0, 45.0], [9340.0, 190.0], [9345.0, 50.0], [9349.83, 0.03], [9406.19, 20.0],
            [9431.0, 5.347], [9450.0, 1.0], [9458.0, 2.0], [9460.0, 0.02], [9489.0, 215.11], [9550.0, 134.357],
            [9562.0, 25.0], [9582.0, 17.304], [9600.0, 21.784], [9640.0, 50.0], [9650.0, 1.0], [9692.0, 1000.0],
            [9715.0, 1.0], [9738.0, 0.5], [9792.0, 1.0], [9800.0, 1.0], [9813.0, 0.5], [9827.0, 50.0], [9990.0, 80.0],
            [9999.0, 1000.0], [10000.0, 2000.0], [10001.0, 50.0], [10119.0, 1.5], [10132.56, 1.957], [10186.56, 0.001],
            [10270.0, 2.0], [10447.0, 25.0], [10500.0, 200.0], [10600.0, 41.954], [71080.0, 1.0]]
    bids = [[9188.75, 53.43], [9187.83, 21.68], [9186.91, 40.64], [9185.99, 24.93], [9185.07, 51.37], [9184.15, 20.09],
            [9183.23, 49.1], [9182.31, 24.39], [9181.39, 20.79], [9181.12, 1.089], [9180.47, 35.67], [9179.55, 21.63],
            [9178.63, 35.59], [9177.71, 52.51], [9177.0, 11.866], [9176.79, 56.2], [9175.87, 37.16], [9168.0, 0.01],
            [9153.25, 0.01], [9150.0, 10.5], [9148.0, 0.01], [9130.0, 1.0], [9128.0, 0.01], [9108.0, 0.01],
            [9106.78, 0.01], [9100.0, 0.5], [9088.0, 0.01], [9080.0, 180.0], [9078.0, 35.0], [9068.0, 0.01],
            [9060.32, 0.011], [9050.0, 0.5], [9048.0, 0.01], [9028.0, 80.0], [9009.0, 7.0], [9002.0, 100.0],
            [9000.0, 40.325], [8999.0, 13.231], [8989.0, 0.1], [8965.0, 5.0], [8961.0, 300.0], [8960.06, 1.0],
            [8955.0, 300.0], [8911.0, 16.254], [8902.0, 340.0], [8900.0, 5.0], [8871.0, 25.0], [8866.42, 0.001],
            [8800.0, 1.0], [8777.0, 38.114], [8705.0, 10.0], [8700.0, 34.173], [8647.17, 10.0], [8600.0, 13.0],
            [8595.0, 20.0], [8550.0, 10.0], [8525.86, 5.823], [8500.0, 3.25], [8488.8, 0.007], [8465.11, 62.411],
            [8450.0, 80.0], [8443.8, 2.047], [8429.4, 0.001], [8400.0, 2.25], [8390.0, 160.0], [8388.0, 2.0],
            [8300.0, 7.25], [8200.0, 2.25], [8100.0, 54.0], [8085.0, 4.52], [8008.0, 3.747], [8000.0, 15.5],
            [7900.0, 124.505], [7855.0, 2.5], [7851.0, 100.0], [7821.0, 0.49], [7803.0, 0.001], [7800.0, 1.0],
            [7760.0, 5.92], [7702.0, 50.0], [7700.0, 1.0], [7675.0, 0.23], [7600.0, 1.0], [7568.3, 0.001],
            [7501.0, 50.0], [7500.0, 1.001], [7421.0, 50.0], [7405.0, 100.0], [7401.0, 100.0], [7011.0, 21.339],
            [7000.0, 206.0], [6986.0, 50.0], [6985.0, 0.076], [6950.0, 0.076], [6942.0, 0.02], [6915.0, 0.076],
            [6879.0, 0.03], [6798.0, 0.02], [6721.0, 100.0], [6450.0, 1.5], [6415.0, 172.154], [6404.95, 0.01],
            [6400.0, 1.0], [6372.92, 0.01], [6358.0, 0.182], [6341.05, 0.01], [6309.34, 0.01], [6301.0, 501.5],
            [6280.56, 0.085], [6277.79, 0.01], [6246.4, 0.01], [6220.0, 200.0], [6215.16, 0.01], [6184.08, 0.01],
            [6153.15, 0.01], [6122.38, 0.01], [6091.76, 0.01], [6061.3, 0.01], [6030.99, 0.01], [6021.0, 30.0],
            [6000.83, 0.01], [6000.0, 16.701]]
    store.orderbooks.add_orderbook('Sandbox', 'BTCUSD', asks, bids)

    # test get_best_ask
    np.testing.assert_equal(
        store.orderbooks.get_best_ask('Sandbox', 'BTCUSD'),
        np.array(
            [9189.0, 52.66]
        )
    )
    # test get_current_asks
    np.testing.assert_equal(
        store.orderbooks.get_current_asks('Sandbox', 'BTCUSD')[0],
        np.array(
            [9189.0, 52.66]
        )
    )
    np.testing.assert_equal(
        store.orderbooks.get_current_asks('Sandbox', 'BTCUSD')[1],
        np.array(
            [9190.0, 27.58]
        )
    )

    # test get_best_bid
    np.testing.assert_equal(
        store.orderbooks.get_best_bid('Sandbox', 'BTCUSD'),
        np.array(
            [9188.0, 53.43]
        )
    )
    # test get_current_bids
    np.testing.assert_equal(
        store.orderbooks.get_current_bids('Sandbox', 'BTCUSD')[0],
        np.array(
            [9188.0, 53.43]
        )
    )
    np.testing.assert_equal(
        store.orderbooks.get_current_bids('Sandbox', 'BTCUSD')[1],
        np.array(
            [9187.0, 21.68]
        )
    )

    # test get_current_orderbook
    np.testing.assert_equal(
        store.orderbooks.get_current_orderbook('Sandbox', 'BTCUSD')[0][0],
        np.array(
            [9189.0, 52.66]
        )
    )

    # test get_orderbooks
    np.testing.assert_equal(
        store.orderbooks.get_orderbooks('Sandbox', 'BTCUSD')[-1][0][0],
        np.array(
            [9189.0, 52.66]
        )
    )


def test_fix_array_len():
    from jesse.store.state_orderbook import _fix_array_len

    a = np.array([
        1, 2, 3, 4, 5
    ], dtype=float)

    a = _fix_array_len(a, 7)
    b = np.array([
        1, 2, 3, 4, 5
    ], dtype=float)

    assert np.array_equiv(a[:5], b)
    assert np.isnan(a[5])
    assert np.isnan(a[6])

    c = np.array([
        1, 2, 3, 4, 5
    ], dtype=float)

    # assert that len has to be >= len(a)
    with pytest.raises(ValueError):
        _fix_array_len(c, 3)
def test_trim_orderbook_list():
    from jesse.store.state_orderbook import _trim_orderbook_list

    trimmed_asks = _trim_orderbook_list(
        [[9414.61, 44.84], [9415.55, 50.31], [9416.49, 49.13], [9417.43, 49.57], [9418.37, 58.71], [9419.31, 40.67],
         [9420.25, 32.2], [9421.19, 32.06], [9422.13, 40.38], [9423.07, 56.83], [9424.01, 53.35], [9424.45, 1.0],
         [9424.95, 35.19], [9425.89, 24.71], [9427.77, 23.11], [9450.0, 10.0], [9454.2, 0.005], [9468.25, 279.229],
         [9470.0, 6.104], [9478.0, 194.239], [9490.0, 0.11], [9500.0, 5.1], [9500.87, 157.017], [9511.0, 20.0],
         [9592.0, 232.788], [9599.0, 0.13], [9600.0, 11.796], [9639.0, 10.0], [9650.0, 1.0], [9692.0, 1000.0],
         [9715.0, 1.0], [9792.0, 1.0], [9800.0, 23.0], [9999.0, 1000.0], [10000.0, 2000.0], [10001.0, 50.0],
         [10119.0, 1.5], [10186.56, 0.001], [10270.0, 2.0], [10500.0, 200.0], [10600.0, 41.954], [71080.0, 1.0]],
        ascending=True
    )
    np.testing.assert_equal(trimmed_asks,
                            [[9415, 44.84], [9416, 50.31], [9417, 49.13], [9418, 49.57], [9419, 58.71], [9420, 40.67],
                             [9421, 32.2],
                             [9422, 32.06], [9423, 40.38], [9424, 56.83], [9425, 89.53999999999999], [9426, 24.71],
                             [9428, 23.11],
                             [9450, 10.0], [9455, 0.005], [9469, 279.229], [9470, 6.104], [9478, 194.239], [9490, 0.11],
                             [9500, 5.1],
                             [9501, 157.017], [9511, 20.0], [9592, 232.788], [9599, 0.13], [9600, 11.796], [9639, 10.0],
                             [9650, 1.0],
                             [9692, 1000.0], [9715, 1.0], [9792, 1.0], [9800, 23.0], [9999, 1000.0], [10000, 2000.0],
                             [10001, 50.0],
                             [10119, 1.5], [10187, 0.001], [10270, 2.0], [10500, 200.0], [10600, 41.954]]
                            )
    trimmed_bids = _trim_orderbook_list(
        [[9414.6, 97.2], [9410.84, 54.62], [9408.96, 41.98], [9408.02, 34.65], [9401.82, 56.84], [9400.88, 23.81],
         [9386.87, 0.005], [9348.25, 7.156], [9346.0, 1.0], [9330.0, 30.0], [9327.13, 100.0], [9303.0, 0.02],
         [9300.99, 1.0], [9300.0, 3.0], [9296.0, 31.0], [9221.0, 7.0], [9200.0, 21.991], [9120.0, 10.0],
         [9080.0, 180.0], [9060.0, 180.0], [9056.0, 30.0], [9028.0, 80.0], [9002.0, 100.0], [9000.0, 41.825],
         [8999.0, 13.231], [8989.0, 0.1], [8970.0, 107.0], [8965.0, 5.0], [8961.0, 300.0], [8960.06, 1.0],
         [8955.0, 300.0], [8940.71, 0.001], [8920.0, 20.0], [8911.0, 16.254], [8909.32, 532.426], [8902.0, 340.0],
         [8900.0, 5.5], [8888.0, 20.0], [8871.92, 0.001], [8800.0, 4.0], [8777.0, 38.114], [8705.0, 10.0],
         [8700.0, 33.173], [8647.17, 10.0], [8600.0, 20.0], [8595.0, 20.0], [8550.0, 35.0], [8525.86, 5.823],
         [8500.0, 1.0], [8488.8, 0.007], [8465.11, 62.411], [8450.0, 80.0], [8429.4, 0.001], [8400.0, 4.5],
         [8390.0, 160.0], [8388.0, 2.0], [8300.0, 6.0], [8200.0, 1.0], [8100.0, 51.5], [8085.0, 4.52], [8008.0, 3.747],
         [8000.0, 14.0], [7900.0, 124.505], [7855.0, 2.5], [7851.0, 100.0], [7821.0, 0.49], [7803.0, 0.001],
         [7800.0, 1.0], [7760.0, 5.92], [7702.0, 50.0], [7700.0, 1.0], [7675.0, 0.23], [7600.0, 1.0], [7568.3, 0.001],
         [7501.0, 50.0], [7500.0, 1.001], [7421.0, 50.0], [7405.0, 100.0], [7401.0, 100.0], [7011.0, 21.339],
         [7000.0, 206.0], [6986.0, 50.0], [6985.0, 0.076], [6950.0, 0.076], [6942.0, 0.02], [6915.0, 0.076],
         [6879.0, 0.03], [6798.0, 0.02], [6721.0, 100.0], [6450.0, 1.5], [6415.0, 172.154], [6404.95, 0.01],
         [6400.0, 1.0], [6372.92, 0.01], [6358.0, 0.182], [6341.05, 0.01], [6309.34, 0.01], [6301.0, 501.5],
         [6280.56, 0.085], [6277.79, 0.01], [6246.4, 0.01], [6220.0, 200.0], [6215.16, 0.01], [6184.08, 0.01],
         [6153.15, 0.01], [6122.38, 0.01], [6091.76, 0.01], [6061.3, 0.01], [6030.99, 0.01], [6021.0, 30.0],
         [6000.83, 0.01], [6000.0, 16.701]],
        ascending=False
    )
    print(trimmed_bids)
    np.testing.assert_equal(
        trimmed_bids,
        [[9414.0, 97.2], [9410.0, 54.62], [9408.0, 76.63], [9401.0, 56.84], [9400.0, 23.81], [9386.0, 0.005],
         [9348.0, 7.156], [9346.0, 1.0], [9330.0, 30.0], [9327.0, 100.0], [9303.0, 0.02], [9300.0, 4.0], [9296.0, 31.0],
         [9221.0, 7.0], [9200.0, 21.991], [9120.0, 10.0], [9080.0, 180.0], [9060.0, 180.0], [9056.0, 30.0],
         [9028.0, 80.0], [9002.0, 100.0], [9000.0, 41.825], [8999.0, 13.231], [8989.0, 0.1], [8970.0, 107.0],
         [8965.0, 5.0], [8961.0, 300.0], [8960.0, 1.0], [8955.0, 300.0], [8940.0, 0.001], [8920.0, 20.0],
         [8911.0, 16.254], [8909.0, 532.426], [8902.0, 340.0], [8900.0, 5.5], [8888.0, 20.0], [8871.0, 0.001],
         [8800.0, 4.0], [8777.0, 38.114], [8705.0, 10.0], [8700.0, 33.173], [8647.0, 10.0], [8600.0, 20.0],
         [8595.0, 20.0], [8550.0, 35.0], [8525.0, 5.823], [8500.0, 1.0], [8488.0, 0.007], [8465.0, 62.411],
         [8450.0, 80.0]]
    )
    assert len(trimmed_bids) == 50


