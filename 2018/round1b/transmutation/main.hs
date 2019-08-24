import qualified Control.Monad as Monad

main = do
    nTests <- read <$> getLine
    Monad.forM_ [1..nTests] $ \i -> do
        nMetals <- read <$> getLine
        formulas' <- Monad.replicateM nMetals getLine
        let formulas = map ((\[a, b] -> (read a - 1, read b - 1)) . words) formulas'
        metalGrams <- map read . words <$> getLine :: IO [Int]
        let ans = solve formulas metalGrams
        putStr $ "Case: #" ++ show i ++ ": " ++ show ans ++ "\n"

solve :: [(Int, Int)] -> [Int] -> Int
solve formulas metalGrams = let maxGram = sum metalGrams
                                minGram = head metalGrams
                             in solve' maxGram minGram formulas metalGrams

-- TODO: binary search is really the best way ?
solve' :: Int -> Int -> [(Int, Int)] -> [Int] -> Int
solve' maxGram minGram formulas metalGrams
    | maxGram == minGram = maxGram
    | maxGram < minGram = error "maxGram is less than minGram"
    | otherwise = let targetGram = half (maxGram + minGram)
                      produceable' = produceable 0 targetGram formulas metalGrams
                   in if produceable' then solve' maxGram targetGram formulas metalGrams
                                      else solve' (targetGram - 1) minGram formulas metalGrams

half n
    | even n = n `div` 2
    | otherwise = (n + 1) `div` 2

-- TODO: correct this function
produceable :: Int -> Int -> [(Int, Int)] -> [Int] -> Bool
produceable index gram formulas metalGrams = let neededGram = gram - metalGrams !! index
                                                 (i1, i2) = formulas !! index
                                              in neededGram <= 0 ||
                                                  (produceable i1 neededGram formulas metalGrams && produceable i2 neededGram formulas metalGrams)
